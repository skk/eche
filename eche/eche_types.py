import typing
from abc import ABCMeta
from collections import OrderedDict, MutableSequence

from attr import attrs, attrib


class EcheTypeBase(object, metaclass=ABCMeta):
    value = None

    def __init__(self, value) -> None:
        super().__init__()
        self.value = value

    def __eq__(self, other: typing.Any) -> bool:
        if isinstance(self, self.__class__) == isinstance(other, self.__class__):
            return self.value == other.value
        else:
            return self.value == other

    def __str__(self) -> str:
        return str(self.value)

    def format_collection(self, prefix_char, collection, suffix_char, sep=' '):
        val = prefix_char + sep.join([str(e) for e in collection]) + suffix_char
        return val


EcheTypeBase.register(list)
EcheTypeBase.register(dict)


@attrs(frozen=True, cmp=False)
class Symbol(EcheTypeBase):
    value = attrib()


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


class Vector(list, EcheTypeBase):
    prefix_char = '['
    suffix_char = ']'

    def __str__(self) -> str:
        if len(self) == 0:
            val = self.prefix_char + self.suffix_char
        else:
            val = self.format_collection(self.prefix_char, self, self.suffix_char)
        return val


@attrs(frozen=False, cmp=False)
class Node(object):
    rest = attrib(default=None)
    data = attrib(default=None)

    @data.validator
    def check(self, attribute, value):
        if attribute == 'data' and isinstance(value, List):
            raise TypeError("data attrib can't be List")

    def __str__(self):
        return str(self.data)

    # def __str__(self):
    #     if self.rest is None:
    #         return self.stringify_pointers()
    #     else:
    #         return f"{self.stringify_pointers()}-->{self.rest}"
    #
    # def stringify_pointers(self):
    #     s = '['
    #     if self.rest:
    #         s += str(self.rest) + (',' if self.data else '')
    #     if self.data:
    #         # <> to distinguish rand from rest
    #         s += f'<{self.data}>'
    #     return s + ']'


@attrs(frozen=False, cmp=False)
class List(MutableSequence, EcheTypeBase):
    def __contains__(self, value):
        return super().__contains__(value)

    head = attrib(default=None)
    length = attrib(default=0)

    def __str__(self) -> str:
        values = [val for val in self]
        val = self.format_collection(self.prefix_char, reversed(values), self.suffix_char)
        return val

    def __iter__(self):
        node = self.head
        while node:
            yield str(node)
            node = node.rest

    # TODO: delete at beginning

    # insert at beginning
    def push(self, new_data) -> None:
        self.length += 1
        new_node = Node(data=new_data, rest=self.head)
        self.head = new_node

    # TODO: delete at middle
    # insert at middle
    def insert_after(self, prev_node, new_data) -> None:

        if prev_node is None:
            raise ValueError("prev_node is None")

        self.length += 1
        prev_node.rest = Node(data=new_data, rest=prev_node)

    # TODO: insert at end
    # delete at end
    def append(self, new_data) -> None:

        new_node = Node(data=new_data)

        if self.head is None:
            self.head = new_node
            self.length += 1
            return

        last = self.head
        while last.rest:
            last = last.rest

        last.rest = new_node

    def __len__(self) -> int:
        return self.length

    def __delitem__(self, index):
        pass

    def insert(self, index, value):
        pass

    def __getitem__(self, index):
        pass

    def __setitem__(self, index, value):
        pass

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
    value = attrib()


@attrs(frozen=True, cmp=False)
class Float(EcheTypeBase):
    value = attrib()
