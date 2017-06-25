from eche.eche_types import Symbol as S, Node, List


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
    pass


special_forms = {
    S('def!'): def_exclamation_mark,
    S('let*'): let_star
}
