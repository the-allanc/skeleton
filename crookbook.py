import six

def essence(attrs):

    def essence_maker(cls):

        def __essence__(self):
            return tuple(getattr(self, attr) for attr in attrs)

        def eq(self, other):
            if isinstance(other, cls):
                return self.__essence__() == cls.__essence__(other)
            return NotImplemented

        # Taken from:
        #   https://stackoverflow.com/a/35781654
        def ne(self, other):
            equal = self.__eq__(other)
            return equal if equal is NotImplemented else not equal

        setattr(cls, '__essence__', __essence__)
        setattr(cls, '__eq__', eq)
        if six.PY2:
            setattr(cls, '__ne__', ne)
        return cls

    return essence_maker
