import typing

from eche.env import get_value
from eche.eche_types import List, Symbol, Node, Vector


def get_data(node: Node) -> typing.Any:
    while isinstance(node, Node):
        if isinstance(node.data, Node):
            node = node.data
        else:
            break

    return node


def eval_ast(ast, env):
    if isinstance(ast, Node):
        ast = ast.data

    if isinstance(ast, str):
        return Symbol(ast)
    elif isinstance(ast, Vector):
        return ast
    elif isinstance(ast, List):
        if len(ast) == 0:
            return ast

        l = List(env=env)

        let_star_found = False

        for node in ast:
            if get_value(node) == 'let*':
                let_star_found = True

            if get_value(node) == 'let*':
                l.append(eval_ast(node, env))
            elif let_star_found:
                l.append(node)
            else:
                l.append(eval_ast(node, env))
        ast = l

        try:
            fn = ast[0].data
        except (IndexError, AttributeError):
            fn = None

        if callable(fn):
            l = List()
            for node in ast:
                l.append(get_data(node))
            l.env = env
            val = fn(l, env=env)
            return val
        else:
            return ast
    elif isinstance(ast, Symbol) and ast in env:
        return env[ast]
    else:
        try:
            return ast.value
        except AttributeError:
            return ast
