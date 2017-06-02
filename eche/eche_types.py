import typing

from attr import attrs, attrib
from collections.abc import MutableSequence

from eche.printer import print_str


class EcheTypeBase(object):
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


@attrs(frozen=True, cmp=False)
class Symbol(EcheTypeBase):
    value = attrib()


# noinspection PyUnresolvedReferences
@attrs(frozen=True, cmp=False)
class String(EcheTypeBase):
    value = attrib()

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


@attrs(frozen=True, cmp=False)
class List(EcheTypeBase, MutableSequence):
    value = attrib(default=list())

    def __getitem__(self, index) -> str:
        return self.value.__getitem__(index)

    def __setitem__(self, index: object, value: typing.Any) -> None:
        self.value.__setitem__(index, value)

    def __len__(self) -> int:
        return len(self.value)

    def __delitem__(self, index: object) -> None:
        self.value.__detitem__(index)

    def pop(self, index=-1):
        return self.value.pop(index)

    def clear(self) -> None:
        self.value.clear()

    def reverse(self) -> None:
        self.value.reverse()

    def remove(self, value: typing.Any) -> None:
        self.value.remove(value)

    def insert(self, index: int, value: typing.Any) -> None:
        self.value.insert(index, value)

    def __str__(self) -> str:
        val = " ".join(map(lambda e: print_str(e), self.value))
        return f"({val})"

    def append(self, rhs: typing.Any) -> None:
        self.value.append(rhs)


@attrs(frozen=True, cmp=False)
class Boolean(EcheTypeBase):
    value = attrib()

    def __str__(self) -> str:
        return 'true' if self.value else 'false'


@attrs(frozen=True, cmp=False)
class Nil(EcheTypeBase):
    value = attrib()


@attrs(frozen=True, cmp=False)
class Atom(EcheTypeBase):
    value = attrib()


@attrs(frozen=True, cmp=False)
class Integer(EcheTypeBase):
    value = attrib()


@attrs(frozen=True, cmp=False)
class Float(EcheTypeBase):
    value = attrib()
