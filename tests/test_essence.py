from crookbook import essence

class ThatBase(object):
    def __init__(self, **kwargs):
        for key, value in kwargs.items():
            setattr(self, 'attr_' + key, value)

@essence(['attr_one'])
class A(ThatBase): pass

@essence(['attr_one', 'attr_two'])
class B(A): pass

@essence(['attr_one'])
class C(ThatBase): pass

@essence(['attr_one', 'attr_two'])
class D(A): pass

class E(A): pass
class F(A): pass

class TestEquality:

    def test_essenceless(self):
        a = A(one=1, two=2)
        tb = ThatBase(one=1, two=2)
        assert not a == tb
        assert a != tb
        assert not tb == a
        assert tb != a

    def test_same_class(self):
        a1 = A(one=1, two=2)
        a2 = A(one=1, two='2')
        a3 = A(one=1)
        a4 = A(one='one')

        assert a1 == a2
        assert a1 == a3
        assert not (a1 == a4)
        assert not (a2 != a3)
        assert a2 != a4
        assert not a3 == a4

    def test_subclass(self):
        a1 = A(one=1, two=2)
        b1 = B(one=1, two=2)
        b2 = B(one=1, two=2, three=3)

        assert a1 == b1
        assert not a1 != b1
        assert not b1 != a1
        assert b1 == a1

        assert a1 == b2
        assert not a1 != b2
        assert not b2 != a1
        assert b2 == a1

    def test_same_essence_but_no_shared_base(self):
        a = A(one=1)
        c = C(one=1)
        assert a != c
        assert not a == c

    def test_same_essence_shared_base_but_diff_class(self):
        b = B(one=1, two=2)
        d = D(one=1, two=2)
        assert b != d
        assert not b == d

    def test_no_reessence_in_base_class(self):
        e = E(one=1)
        e.three = 3
        f = F(one=1)
        f.four = 4
        assert e == f
        assert not e != f

