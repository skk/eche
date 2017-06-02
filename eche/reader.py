import re
import typing

from eche.eche_types import Symbol, List, String, Boolean, Nil, Integer, Float, EcheTypeBase


class Blank(Exception):
    pass


int_re = re.compile(r"-?[0-9]+")
float_re = re.compile(r"-?[0-9][0-9.]*")


class Reader(object):
    def __init__(self, tokens: typing.List[str], position: int=0) -> None:
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
    tre = re.compile(r"""[\s,]*(~@|[\[\]{}()'`~^@]|"(?:[\\].|[^\\"])*"?|;.*|[^\s\[\]{}()'"`@,;]+)""")
    tokens = [t for t in re.findall(tre, data) if t[0] != ';']
    return tokens


def read_form(reader: Reader) -> typing.Union[None, typing.List[typing.Any], EcheTypeBase]:
    token = reader.peek()
    # print(f"read_form token {token}")

    if token[0] == ';':
        reader.next()
        return None
    # list
    elif token == ')':
        raise SyntaxError("unexpected ')'")
    elif token == '(':
        return read_list(reader)
    # atom
    else:
        return read_atom(reader)


def read_list(reader: Reader) -> List:
    return read_sequence(reader, '(', ')')


def read_sequence(reader: Reader, start='(', end=')') -> typing.List[typing.Any]:
    ast = List(list())
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
            ast.append(val)
        token = reader.peek()

    reader.next()
    return ast


def _unescape(s: str) -> str:
    return s.replace('\\"', '"').replace('\\n', '\n').replace('\\\\', '\\')


def read_atom(reader: Reader) -> EcheTypeBase:
    token = reader.next()

    # print(f"read_atom token {token}")

    if re.match(int_re, token):
        # print(f"int atom {token}")
        atom = Integer(token)
    elif re.match(float_re, token):
        # print(f"float atom {token}")
        atom = Float(token)
    elif token[0] == '"':
        if token[-1] == '"':
            return String(token[1:-1])
        else:
            raise ValueError("expected '\"', got EOF")
    elif token == 'nil':
        # print(f"nil atom {token}")
        atom = Nil(None)
    elif token == 'false':
        # print(f"false atom {token}")
        atom = Boolean(False)
    elif token == 'true':
        # print(f"true atom {token}")
        atom = Boolean(True)
    else:
        # print(f"symbol atom {token}")
        atom = Symbol(token)

    # print(f"token {token} atom {atom}")
    return atom
