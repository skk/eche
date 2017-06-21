from eche.eche_types import Node, Symbol as S, Env
from eche.special_forms import special_forms


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

env = Env()
env.data.update({
    S('+'): add,
    S('-'): subtract,
    S('*'): multiply,
    S('/'): divide,
    S('^'): exp,
    S('%'): mod,
})

env.data.update(special_forms)
