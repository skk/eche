import operator

from eche.eche_types import List, Symbol, Node

repl_env = {
    Symbol('+'): operator.add,
    Symbol('-'): operator.sub,
    Symbol('*'): operator.mul,
    Symbol('/'): operator.truediv,
    Symbol('^'): operator.pow,
    Symbol('%'): operator.mod
}


def eval_ast(ast, env):
    if env is None:
        env = repl_env

    if isinstance(ast, Node):
        ast = ast.data

    if isinstance(ast, List):
        if len(ast) == 0:
            return ast

        new_list = List()
        for idx, node in enumerate(ast):
            val = eval_ast(node, env)
            new_list.prepend(val)

        try:
            fn = new_list[0].data
        except IndexError:
            return new_list
        else:
            if callable(fn):
                data = [d.data for d in new_list[1:]]
                val = fn.__call__(*data)
                return val
    elif isinstance(ast, Symbol):
        return env[ast]
    else:
        return ast.value
