import typing

from eche.eche_types import Node, Symbol, Env
from eche.special_forms import special_forms


def get_value(node):
    try:
        return node.data.value
    except AttributeError:
        try:
            return node.data
        except AttributeError:
            return node


def multiply(ast: typing.List[Node], env: Env) -> Node:
    _, a, b = ast
    a = get_value(a)
    b = get_value(b)
    data = a * b
    return Node(data=data, env=env)


def add(ast: typing.List[Node], env: Env) -> Node:
    _, a, b = ast
    a = get_value(a)
    b = get_value(b)
    data = a + b
    return Node(data=data, env=env)


def subtract(ast: typing.List[Node], env: Env) -> Node:
    _, a, b = ast
    a = get_value(a)
    b = get_value(b)
    data = a - b
    return Node(data=data, env=env)


def divide(ast: typing.List[Node], env: Env) -> Node:
    _, a, b = ast
    a = get_value(a)
    b = get_value(b)
    data = a / b
    return Node(data=data, env=env)


def exp(ast: typing.List[Node], env: Env) -> Node:
    _, a, b = ast
    a = get_value(a)
    b = get_value(b)
    data = pow(a, b)
    return Node(data=data, env=env)


def mod(ast: typing.List[Node], env: Env) -> Node:
    _, a, b = ast
    a = get_value(a)
    b = get_value(b)
    data = a % b
    return Node(data=data, env=env)


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
