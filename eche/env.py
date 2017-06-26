import typing

from eche.eche_types import Node, Symbol, Env
from eche.special_forms import special_forms


def multiply(ast: typing.List[Node]) -> Node:
    _, a, b = ast
    return Node(data=a.data * b.data)


def add(ast: typing.List[Node]) -> Node:
    _, a, b = ast
    return Node(data=a.data + b.data)


def subtract(ast: typing.List[Node]) -> Node:
    _, a, b = ast
    return Node(data=a.data - b.data)


def divide(ast: typing.List[Node]) -> Node:
    _, a, b = ast
    return Node(data=a.data / b.data)


def exp(ast: typing.List[Node]) -> Node:
    _, a, b = ast
    return Node(data=pow(a.data, b.data))


def mod(ast: typing.List[Node]) -> Node:
    _, a, b = ast
    return Node(data=a.data % b.data)


def get_default_env():
    env = Env()
    env.data.update({
        Symbol('+'): add,
        Symbol('-'): subtract,
        Symbol('*'): multiply,
        Symbol('/'): divide,
        Symbol('^'): exp,
        Symbol('%'): mod,
    })
    env.data.update(special_forms)
    return env
