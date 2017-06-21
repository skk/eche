import typing

from eche.eche_types import List, Symbol, Node, Vector
from eche.env import env


def get_data(node: Node) -> typing.Any:
    while isinstance(node, Node):
        if isinstance(node.data, Node):
            node = node.data
        else:
            break

    return node


def eval_ast(ast, _env):
    if _env is None:
        _env = env

    if isinstance(ast, Node):
        ast = ast.data

    if isinstance(ast, Vector):
        return ast
    elif isinstance(ast, List):
        if len(ast) == 0:
            return ast

        ast = [Node(data=eval_ast(node, _env)) for node in ast]
        try:
            fn = ast[0].data
        except (IndexError, AttributeError):
            fn = None

        if callable(fn):
            ast = [get_data(node) for node in ast]
            val = fn(*ast[1:])
            return val
        else:
            return ast
    elif isinstance(ast, Symbol):
        return _env[ast]
    else:
        return ast.value
