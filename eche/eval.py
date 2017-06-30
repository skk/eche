from eche.eche_types import List, Symbol, Node, Vector


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

        new_ast = List(env=env)

        let_star_found = False

        for idx, node in enumerate(ast):
            if node.get_value() == 'let*':
                let_star_found = True
                new_ast.append(eval_ast(node, env))
            elif let_star_found:
                new_ast.append(node)
            else:
                new_ast.append(eval_ast(node, env))

        try:
            fn = new_ast.head.data
        except AttributeError:
            return new_ast
        else:
            if callable(fn):
                try:
                    val = fn(new_ast, env=env)
                except TypeError as e:
                    pass
                else:
                    return val
            else:
                return new_ast
    elif isinstance(ast, Symbol) and ast in env:
        return env[ast]
    else:
        return ast
