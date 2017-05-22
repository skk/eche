from attr import attrs, attrib


# @attrs(frozen=True, cmp=False)
class EcheTypeBase(object):
    def __eq__(self, other):
        if isinstance(self, self.__class__) == isinstance(other, self.__class__):
            return self.value == other.value
        else:
            return self.value == other


@attrs(frozen=True, cmp=False)
class Symbol(EcheTypeBase):
    value = attrib()


@attrs(frozen=True, cmp=False)
class String(EcheTypeBase):
    value = attrib()

    def __eq__(self, other):
        if isinstance(self, self.__class__) == isinstance(other, self.__class__):
            if self.value[0] == '\"' and self.value[-1] == '\"':
                if other.value[0] == '\"' and other.value[-1] == '\"':
                    return self.value == other.value
                else:
                    return self.value == f'"{other.value}"'
        else:
            return self.value == other


# lists
# @attrs(frozen=True, cmp=False)
class List(list):
    # def __add__(self, rhs):
    #     return List(list.__add__(self, rhs))
    #
    # def __getitem__(self, i):
    #     if type(i) == slice:
    #         return List(list.__getitem__(self, i))
    #     elif i >= len(self):
    #         return None
    #     else:
    #         return list.__getitem__(self, i)
    #
    # def __getslice__(self, *a):
    #     return List(self.__getslice__(self, *a))

    @classmethod
    def is_list(cls, obj):
        return isinstance(obj, cls)


@attrs(frozen=True, cmp=False)
class Boolean(EcheTypeBase):
    value = attrib()

    @classmethod
    def is_boolean(cls, exp):
        return isinstance(exp, cls)

    def __eq__(self, other):
        return super().__eq__(other)


@attrs(frozen=True, cmp=False)
class Nil(EcheTypeBase):
    value = attrib()

    @classmethod
    def is_nil(cls, exp):
        return isinstance(exp, cls)

    def __eq__(self, other):
        return super().__eq__(other)


@attrs(frozen=True, cmp=False)
class Atom(EcheTypeBase):
    value = attrib()

    @classmethod
    def is_atom(cls, exp):
        return isinstance(exp, Atom)
