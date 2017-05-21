from eche_types import List, Nil, Atom, Boolean


def print_str(obj):
    return str(obj)
    # if List.is_list(obj):
    #     val = " ".join(map(lambda e: print_str(e), obj))
    #     return f"({val})"
    # elif Nil.is_nil(obj):
    #     return "nil"
    # elif Boolean.is_boolean(obj) and bool(obj):
    #     return "true"
    # elif Boolean.is_boolean(obj) and not bool(obj):
    #     return "false"
    # elif Atom.is_atom(obj):
    #     val = print_str(obj.value)
    #     return f"(atom {val})"
    # else:
    #     return str(obj)
