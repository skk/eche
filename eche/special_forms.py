from funcy.seqs import partition

from eche.eche_types import Symbol, List, Env


# noinspection PyUnusedLocal
def def_exclamation_mark(ast, env: Env):
    from eche.eval import eval_ast

    _, key, val = ast
    l = List()
    l.append(key)
    l.append(val)
    l.env = ast.env

    _, val = eval_ast(l, ast.env)
    ast.env[key] = val

    return ast


def let_star(ast, env: Env):
    from eche.env import get_default_env
    from eche.eval import eval_ast

    inner_env = get_default_env()
    inner_env.outer = env

    _, new_bindings, commands_in_new_env = ast

    new_bindings = partition(2, list(new_bindings.data))

    for binding in new_bindings:
        key, val = binding
        inner_env[key] = val

    commands_in_new_env = eval_ast(commands_in_new_env, inner_env)
    new_ast = eval_ast(commands_in_new_env, inner_env)
    return new_ast


special_forms = {
    Symbol('def!'): def_exclamation_mark,
    Symbol('let*'): let_star
}
