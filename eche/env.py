from eche.eche_types import Node, Symbol, Env


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
    Symbol('+'): add,
    Symbol('-'): subtract,
    Symbol('*'): multiply,
    Symbol('/'): divide,
    Symbol('^'): exp,
    Symbol('%'): mod
})
