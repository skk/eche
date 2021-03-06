import typing
import operator

from functools import reduce

from eche.eche_types import Node, Symbol, Env
from eche.special_forms import special_forms


def arithmetic_fn_reduction(ast, arithmetic_fn, env, initializer=None):
    ast = [a.get_value() for a in iter(ast[1:])]
    if initializer is None:
        data = reduce(arithmetic_fn, ast)
    else:
        data = reduce(arithmetic_fn, ast, initializer)
    return Node(data=data, env=env)


def multiply(ast: typing.List[Node], env: Env) -> Node:
    return arithmetic_fn_reduction(ast, operator.mul, env, 1)


def add(ast: typing.List[Node], env: Env) -> Node:
    return arithmetic_fn_reduction(ast, operator.add, env, 0)


def subtract(ast: typing.List[Node], env: Env) -> Node:
    return arithmetic_fn_reduction(ast, operator.sub, env)


def divide(ast: typing.List[Node], env: Env) -> Node:
    return arithmetic_fn_reduction(ast, operator.truediv, env)


def exp(ast: typing.List[Node], env: Env) -> Node:
    return arithmetic_fn_reduction(ast, operator.pow, env)


def mod(ast: typing.List[Node], env: Env) -> Node:
    return arithmetic_fn_reduction(ast, operator.mod, env)


def print_(ast: typing.List[Node], env: Env) -> None:
    _, value, *rest = ast
    print(value)


def get_default_env():
    env = Env()
    env.data.update({
        Symbol('+'): add,
        Symbol('-'): subtract,
        Symbol('*'): multiply,
        Symbol('/'): divide,
        Symbol('^'): exp,
        Symbol('%'): mod,
        Symbol('print'): print_,
    })
    env.data.update(special_forms)
    return env
