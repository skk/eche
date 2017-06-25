import typing

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

    if isinstance(ast, Vector):
        return ast
    elif isinstance(ast, List):
        if len(ast) == 0:
            return ast

        l = List(env=env)
        for node in ast:
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
            val = fn(l)
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
