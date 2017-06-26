from eche.eche_types import Symbol, List


def def_exclamation_mark(ast):
    from eche.eval import eval_ast

    _, key, val = ast
    l = List()
    l.append(key)
    l.append(val)
    l.env = ast.env

    _, val = eval_ast(l, ast.env)
    ast.env[key] = val
    # if not isinstance(ast, Node):
    #     ast = Node(data=ast)

    return ast


def let_star(*args, env=None):
    pass  # pragma: no cover


special_forms = {
    Symbol('def!'): def_exclamation_mark,
    Symbol('let*'): let_star
}
