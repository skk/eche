from eche.eche_types import Symbol as S, Node


def def_exclamation_mark(*args, _env=None):
    from eche.eval import eval_ast
    from eche.env import env

    if _env is None:
        _env = env

    key, ast = args
    ast = eval_ast(ast, _env=_env)
    _env[key] = ast
    if not isinstance(ast, Node):
        ast = Node(data=ast)

    return ast


def let_star(*args, env=None):
    pass


special_forms = {
    S('def!'): def_exclamation_mark,
    S('let*'): let_star
}
