from re import compile, match, findall
import typing

from funcy.seqs import chunks

from eche.eche_types import Symbol, String, Boolean, Nil, Integer, Float, EcheTypeBase, Dict, \
    Vector, List


class Blank(Exception):
    pass


int_re = compile(r"-?[0-9]+")
float_re = compile(r"-?[0-9][0-9.]*")


class Reader(object):
    def __init__(self, tokens: typing.List[str], position: int=0):
        self.tokens = tokens
        self.position = position

    def next(self) -> typing.Any:
        self.position += 1
        return self.tokens[self.position - 1]

    def peek(self) -> typing.Union[str, None]:
        if len(self.tokens) > self.position:
            return self.tokens[self.position]
        else:
            return None


def read_str(data: str) -> typing.List[typing.Any]:
    # print(f"read-str data {data}")
    tokens = tokenize(data)
    # print(f"read-str tokens {tokens}")
    if len(tokens) == 0:
        raise Blank("Blank Line")
    reader = Reader(tokens)
    forms = read_form(reader)
    return forms


def tokenize(data: str) -> typing.List[str]:
    tre = compile(r"""[\s,]*(~@|[\[\]{}()'`~^@]|"(?:[\\].|[^\\"])*"?|;.*|[^\s\[\]{}()'"`@,;]+)""")
    tokens = [t for t in findall(tre, data) if t[0] != ';']
    return tokens


def read_form(reader: Reader) -> typing.Union[None, typing.List[typing.Any], EcheTypeBase]:
    token = reader.peek()
    # print(f"read_form token {token}")

    if token[0] == ';':
        reader.next()
        return None
    # vector
    elif token == Vector.suffix_char:
        raise SyntaxError(f"unexpected '{Vector.suffix_char}'")
    elif token == Vector.prefix_char:
        return read_vector(reader)
    # dict
    elif token == Dict.suffix_char:
        raise SyntaxError(f"unexpected '{Dict.suffix_char}'")
    elif token == Dict.prefix_char:
        return read_dict(reader)
    # list
    elif token == List.suffix_char:
        raise SyntaxError(f"unexpected '{List.suffix_char}'")
    elif token == List.prefix_char:
        return read_list(reader)
    # atom
    else:
        return read_atom(reader)


def read_vector(reader: Reader) -> Vector:
    vec = Vector()
    for val in read_sequence(reader, Vector.prefix_char, Vector.suffix_char):
        vec.append(val)

    return vec


def read_list(reader: Reader) -> List:
    linked_list = List()
    for val in read_sequence(reader, List.prefix_char, List.suffix_char):
        linked_list.append(val)
    return linked_list


def read_dict(reader: Reader) -> Dict:
    d = Dict()
    for key, val in chunks(2, read_sequence(reader, Dict.prefix_char, Dict.suffix_char)):
        d[key] = val

    return d


def read_sequence(reader: Reader, start: str, end: str) -> typing.List[typing.Any]:
    token = reader.next()
    if token != start:
        raise SyntaxError(f"expected '{start}'")

    token = reader.peek()
    while token != end:
        if not token:
            raise SyntaxError(f"expected '{end}', got EOF")

        try:
            val = read_form(reader)
        except SyntaxError as e:
            print(e)
        else:
            yield val
        finally:
            token = reader.peek()

    reader.next()


def _unescape(s: str) -> str:
    return s.replace('\\"', '"').replace('\\n', '\n').replace('\\\\', '\\')


def read_atom(reader: Reader) -> EcheTypeBase:
    token = reader.next()

    # print(f"read_atom token {token}")

    if match(int_re, token) or match(float_re, token):
        try:
            atom = Integer(token)
        except ValueError:
            pass
        else:
            return atom

        try:
            atom = Float(token)
        except ValueError:
            pass
        else:
            return atom
    elif token[0] == '"':
        if token[-1] == '"':
            return String(token[1:-1])
        else:
            raise ValueError("expected '\"', got EOF")
    elif token == 'nil':
        atom = Nil(None)
    elif token == 'false':
        atom = Boolean(False)
    elif token == 'true':
        atom = Boolean(True)
    else:
        atom = Symbol(token)

    return atom
