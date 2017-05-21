from attr import attrs, attrib


class EcheTypeBase(object):
    pass


@attrs(frozen=True)
class Symbol(EcheTypeBase):
    value = attrib()


@attrs(frozen=True)
class String(EcheTypeBase):
    value = attrib(convert=lambda v: f'"{v}"')


# lists
class List(list):
    def __add__(self, rhs):
        return List(list.__add__(self, rhs))

    def __getitem__(self, i):
        if type(i) == slice:
            return List(list.__getitem__(self, i))
        elif i >= len(self):
            return None
        else:
            return list.__getitem__(self, i)

    def __getslice__(self, *a):
        return List(self.__getslice__(self, *a))

    @classmethod
    def is_list(cls, obj):
        return isinstance(obj, cls)


class Boolean(object):
    def __init__(self, val):
        self.val = val

    @classmethod
    def is_boolean(cls, exp):
        return isinstance(exp, cls)


@attrs(frozen=True)
class Nil(EcheTypeBase):
    value = attrib()

    @classmethod
    def is_nil(cls, exp):
        return isinstance(exp, cls)


@attrs(frozen=True)
class Atom(EcheTypeBase):
    value = attrib()

    @classmethod
    def is_atom(cls, exp):
        return isinstance(exp, Atom)
