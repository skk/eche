import re

from eche_types import Symbol, List


class Blank(Exception):
    pass


class Reader(object):
    def __init__(self, tokens, position=0):
        self.tokens = tokens
        self.position = position

    def next(self):
        self.position += 1
        return self.tokens[self.position - 1]

    def peek(self):
        if len(self.tokens) > self.position:
            return self.tokens[self.position]
        else:
            return None


def read_str(data):
    # print(f"read-str data {data}")
    tokens = tokenize(data)
    # print(f"read-str tokens {tokens}")
    if len(tokens) == 0:
        raise Blank("Blank Line")
    return read_form(Reader(tokens))


def tokenize(data):
    token_re = re.compile(r"""[\s,]*(~@|[\[\]{}()'`~^@]|"(?:[\\].|[^\\"])*"?|;.*|[^\s\[\]{}()'"`@, ;]+)""")
    return [t for t in re.findall(token_re, data) if t[0] != ';']


def read_form(reader):
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


def read_list(reader):
    return read_sequence(reader, List, '(', ')')


def read_sequence(reader, typ=list, start='(', end=')'):
    ast = typ()
    token = reader.next()
    if token != start:
        raise SyntaxError(f"expected '{start}'")

    token = reader.peek()
    while token != end:
        if not token:
            raise SyntaxError(f"expected '{end}', got EOF")
        ast.append(read_form(reader))
        token = reader.peek()
    reader.next()
    return ast


def read_atom(reader):
    int_re = re.compile(r"-?[0-9]+$")
    float_re = re.compile(r"-?[0-9][0-9.]*$")
    token = reader.next()

    # print(f"read_atom token {token}")

    if re.match(int_re, token):
        # print(f"int atom {token}")
        atom = int(token)
    elif re.match(float_re, token):
        # print(f"float atom {token}")
        atom = float(token)
    elif token == 'nil':
        # print(f"nil atom {token}")
        atom = None
    elif token == 'false':
        # print(f"false atom {token}")
        atom = False
    elif token == 'true':
        # print(f"true atom {token}")
        atom = True
    else:
        # print(f"symbol atom {token}")
        atom = Symbol(token)

    # print(f"token {token} atom {atom}")
    return atom
