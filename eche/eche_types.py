import typing
from abc import ABCMeta
from collections import OrderedDict, MutableSequence, MutableMapping

from attr import attrs, attrib


class EcheTypeBase(object, metaclass=ABCMeta):
    value = None

    def __init__(self, value) -> None:
        self.value = value

    def __eq__(self, other: typing.Any) -> bool:
        if isinstance(self, self.__class__) == isinstance(other, self.__class__):
            return self.value == other.value
        else:
            return self.value == other

    def __str__(self) -> str:
        return str(self.value)

    def format_collection(self, prefix_char, collection, suffix_char, sep=' '):
        val = prefix_char + sep.join([str(e)
                                      for e in collection
                                      if e is not None or e is not END_NODE]) + suffix_char
        return val


EcheTypeBase.register(list)
EcheTypeBase.register(dict)


@attrs(frozen=True, cmp=False)
class Symbol(EcheTypeBase):
    value = attrib()

    def __hash__(self) -> int:
        return hash(self.value)


@attrs(frozen=True, cmp=False)
class Keyword(EcheTypeBase):
    value = attrib()

    def __hash__(self) -> int:
        return hash(self.value)


# noinspection PyUnresolvedReferences
@attrs(frozen=True, cmp=False)
class String(EcheTypeBase):
    value = attrib()

    def __hash__(self) -> int:
        return self.value.__hash__()

    def __str__(self) -> str:
        return f'"{self.value}"'

    def __eq__(self, other) -> bool:
        if isinstance(self, self.__class__) == isinstance(other, self.__class__):
            if self.value[0] == '\"' and self.value[-1] == '\"':
                if other.value[0] == '\"' and other.value[-1] == '\"':
                    return self.value == other.value
                else:
                    return self.value == f'"{other.value}"'

        return self.value == other


class Dict(OrderedDict, EcheTypeBase):
    prefix_char = '{'
    suffix_char = '}'

    def __str__(self) -> str:
        values = []
        for key in self.keys():
            val = self[key]
            values.append(f"{key} {val}")

        val = self.format_collection(self.prefix_char, values, self.suffix_char)
        return val


@attrs(frozen=False, cmp=False)
class Env(MutableMapping):
    outer = attrib(default=None)
    data = attrib(default=None)

    def __attrs_post_init__(self):
        self.data = Dict()

    def __delitem__(self, key: Symbol):
        del self.data[key]

    def __setitem__(self, key: Symbol, value: object):
        self.data[key] = value

    def __len__(self) -> int:
        return len(self.data)

    def __iter__(self) -> object:
        return iter(self.data)

    def __getitem__(self, key: Symbol) -> object:
        return self.data[key]

    def find(self, key: Symbol) -> object:
        try:
            return self[key]
        except KeyError:
            if self.outer is None:
                raise
            else:
                return self.outer.find(key)


class Vector(list, EcheTypeBase):
    prefix_char = '['
    suffix_char = ']'

    def __str__(self) -> str:
        val = self.format_collection(self.prefix_char, self, self.suffix_char)
        return val


def node_data_convert(val):
    if isinstance(val, Node):
        return val.data
    else:
        return val


@attrs(frozen=False, cmp=False)
class Node(object):
    def __hash__(self) -> int:
        return hash(self.data)

    rest = attrib(default=None)
    data = attrib(default=None, convert=node_data_convert)
    env = attrib(default=None)

    @data.validator
    def check(self, attribute, value):
        if attribute == 'data' and isinstance(value, List):
            raise TypeError("data attrib can't be List")

    def __eq__(self, o) -> bool:
        try:
            val = o.data
        except AttributeError:
            val = o

        return self.data == val

    def __str__(self) -> str:
        return str(self.data)

END_NODE = Node()


@attrs(frozen=False, cmp=False)
class List(MutableSequence, EcheTypeBase):
    env = attrib(default=Env())
    head = attrib(default=END_NODE)
    length = attrib(default=0)

    # TODO: delete at beginning
    # TODO: delete at middle

    # insert at end
    def append(self, new_data) -> None:
        new_node = Node(data=node_data_convert(new_data))

        if self.head is END_NODE or self.head is None:
            self.head = new_node
        else:
            last = self.head
            while last.rest:
                last = last.rest
            last.rest = new_node

        self.length += 1

    # insert at middle
    def insert_after(self, prev_node, new_data) -> None:
        raise NotImplementedError

    # insert at beginning
    def prepend(self, new_data: typing.Union[Node, EcheTypeBase]) -> None:
        new_node = Node(data=node_data_convert(new_data))

        if self.head is END_NODE or self.head is None:
            self.head = new_node
        else:
            new_node.rest = self.head.rest
            self.head = new_node
        self.length += 1

    def __len__(self) -> int:
        return self.length

    def __delitem__(self, index):
        pass

    def insert(self, index, value):
        pass

    def __getitem__(self, index):
        vals = []
        for idx, node in enumerate(self):
            if isinstance(index, slice):
                start = index.start
                if idx >= start:
                    vals.append(node)
            else:
                if idx == index:
                    return node

        if isinstance(index, slice) and len(vals) > 0:
            return vals

        raise IndexError

    def __setitem__(self, index, value):
        for idx, node in enumerate(self):
            if idx == index:
                node.value = value
        raise IndexError

    def __str__(self) -> str:
        values = [val for val in self if val.data is not None]
        val = self.format_collection(self.prefix_char, values, self.suffix_char)
        return val

    def __iter__(self):
        node = self.head
        while node:
            yield node
            node = node.rest

    def __contains__(self, value):
        for val in self:
            if val == value:
                return True

        return False

    prefix_char = '('
    suffix_char = ')'


@attrs(frozen=True, cmp=False)
class Boolean(EcheTypeBase):
    value = attrib()

    def __str__(self) -> str:
        return 'true' if self.value else 'false'


@attrs(frozen=True, cmp=False)
class Nil(EcheTypeBase):
    value = attrib()

    def __str__(self) -> str:
        return 'nil'


@attrs(frozen=True, cmp=False)
class Atom(EcheTypeBase):
    value = attrib()


@attrs(frozen=True, cmp=False)
class Integer(EcheTypeBase):
    value = attrib(convert=lambda x: int(x, base=10))


@attrs(frozen=True, cmp=False)
class Float(EcheTypeBase):
    value = attrib(convert=lambda x: float(x))
