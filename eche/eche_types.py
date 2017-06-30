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


@attrs(frozen=False, cmp=False)
class Node(object):
    def __hash__(self) -> int:
        return hash(self.data)

    next = attrib(default=None)
    data = attrib(default=None)
    env = attrib(default=None)

    def get_value(self):
        if isinstance(self.data, EcheTypeBase):
            return self.data.value
        else:
            return self.data

    @data.validator
    def check(self, attribute, value):
        if isinstance(value, Node):
            self.data = value.data

        if attribute == 'data':
            if isinstance(value, List):
                raise TypeError("data attrib can't be List")

    def __iter__(self):
        node = self.next
        while next:
            yield node.get_value()
            node = node.next

    def __eq__(self, o) -> bool:
        try:
            val = o.data
        except AttributeError:
            val = o

        return self.data == val

    def __str__(self) -> str:
        return str(self.data)

    def __repr__(self) -> str:
        return repr(self.data)

END_NODE = Node()


@attrs(frozen=False, cmp=False)
class List(MutableSequence, EcheTypeBase):
    env = attrib(default=Env())
    head = attrib(default=None)
    length = attrib(default=0)

    # TODO: delete at beginning
    # TODO: delete at middle

    # insert at end
    def append(self, data: EcheTypeBase) -> None:
        if not self.head:
            self.head = Node(data=data)
            return

        current = self.head
        while current and current.next:
            current = current.next
        current.next = Node(data=data)

        self.length += 1

    # insert at middle
    def insert_after(self, prev_node, data) -> None:
        raise NotImplementedError

    # insert at beginning
    def prepend(self, data: EcheTypeBase) -> None:
        self.head = Node(data=data, next=self.head)
        self.length += 1

    def __len__(self) -> int:
        return self.length

    def __delitem__(self, index):
        pass

    def insert(self, index, value):
        pass

    def __getitem__(self, index):
        values = []
        for idx, node in enumerate(self):
            if isinstance(index, slice):
                start = index.start
                if idx >= start:
                    values.append(node)
            else:
                if idx == index:
                    return node

        if isinstance(index, slice) and len(values) > 0:
            return values

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

    def __repr__(self):
        nodes = [node for node in iter(self)]
        return '[' + ', '.join(nodes) + ']'

    def __iter__(self):
        node = self.head
        while node:
            yield node
            node = node.next

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
