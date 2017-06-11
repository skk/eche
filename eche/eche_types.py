import typing
from abc import ABCMeta

from attr import attrs, attrib
from collections import OrderedDict


from eche.printer import print_str


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
        buf = []
        for key in self.keys():
            val = self[key]
            buf.append(f"{key} {val}")

        buf = ' '.join(buf)
        buf = self.prefix_char + f'{buf}' + self.suffix_char

        return buf


class Vector(list, EcheTypeBase):
    prefix_char = '['
    suffix_char = ']'

    def __str__(self) -> str:
        if len(self) == 0:
            val = self.prefix_char + self.suffix_char
        else:
            val = self.prefix_char + ' '.join([str(e) for e in self]) + self.suffix_char
        return val


@attrs(frozen=True, cmp=False)
class List(list, EcheTypeBase):
    prefix_char = '('
    suffix_char = ')'

    def __str__(self) -> str:
        val = " ".join(map(lambda e: print_str(e), self))
        return self.prefix_char + f"{val}" + self.suffix_char


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
