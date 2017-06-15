from eche.eche_types import List, Symbol, Node


def multiply(a: Node, b: Node) -> Node:
    return Node(data=a.data * b.data)


def add(a: Node, b: Node) -> Node:
    return Node(data=a.data + b.data)


def subtract(a: Node, b: Node) -> Node:
    return Node(data=a.data - b.data)


def divide(a: Node, b: Node) -> Node:
    return Node(data=a.data / b.data)


def exp(a: Node, b: Node) -> Node:
    return Node(data=pow(a.data, b.data))


def mod(a: Node, b: Node) -> Node:
    return Node(data=a.data % b.data)


repl_env = {
    Symbol('+'): add,
    Symbol('-'): subtract,
    Symbol('*'): multiply,
    Symbol('/'): divide,
    Symbol('^'): exp,
    Symbol('%'): mod
}


def eval_ast(ast, env):
    if env is None:
        env = repl_env

    if isinstance(ast, Node):
        ast = ast.data

    if isinstance(ast, List):
        if len(ast) == 0:
            return ast

        ast = [Node(data=eval_ast(node, env)) for node in ast]
        try:
            fn = ast[0].data
        except (IndexError, AttributeError):
            fn = None

        if callable(fn):
            vals = fn(*ast[1:])
            return vals
        else:
            return ast
    elif isinstance(ast, Symbol):
        return env[ast]
    else:
        return ast.value
