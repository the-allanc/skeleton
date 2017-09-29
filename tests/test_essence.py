from crookbook import essence
import operator
import pytest
import six

class ThatBase(object):
    def __init__(self, **kwargs):
        for key, value in kwargs.items():
            setattr(self, 'attr_' + key, value)

@essence(['attr_one'])
class A(ThatBase): pass

@essence(['attr_one', 'attr_two'], mutable=False)
class B(A): pass

@essence(['attr_one'])
class C(ThatBase): pass

@essence(['attr_one', 'attr_two'])
class D(A): pass

class E(A): pass
class F(A): pass

@essence(['attr_two', 'attr_one'])
class G(A): pass


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


class TestOrdering:

    @staticmethod
    def assert_incomparable(val1, strcomp, val2):
        func = getattr(operator, strcomp)
        if six.PY2:
            res = func(val1, val2)
            assert res in (False, True)  # doesnt matter what the actual result is
        else:
            pytest.raises(TypeError, func, val1, val2)

    def test_essenceless(self):
        a = A(one=1, two=2)
        tb = ThatBase(one=1, two=2)
        self.assert_incomparable(a, 'lt', tb)
        self.assert_incomparable(a, 'ge', tb)
        self.assert_incomparable(tb, 'lt', a)
        self.assert_incomparable(tb, 'gt', a)

    def test_same_class(self):
        a1 = A(one=1, two=2)
        a2 = A(one=2, two='2')
        a3 = A(one=1)
        a4 = A(one='one')

        assert a1 < a2
        assert a1 <= a2
        assert not (a1 > a2)
        assert not (a1 >= a2)
        assert a2 >= a1
        assert not a3 < a1
        assert not a3 > a1

    def test_subclass(self):
        a1 = A(one=1, two=2)
        b1 = B(one=2, two=2)
        b2 = B(one=1, two=2, three=3)

        assert a1 < b1
        assert a1 <= b1
        assert not a1 > b2
        assert a1 >= b2

        assert not b1 < a1
        assert not b1 <= a1
        assert not b2 > a1
        assert b2 >= a1

        assert not a1 > b1
        assert not a1 < b2
        assert a1 <= b2
        assert b1 >= a1

    def test_same_essence_but_no_shared_base(self):
        a = A(one=1)
        c = C(one=1)
        self.assert_incomparable(a, 'lt', c)

    def test_same_essence_shared_base_but_diff_class(self):
        b = B(one=1, two=2)
        d = D(one=1, two=2)
        self.assert_incomparable(b, 'gt', d)

    def test_no_reessence_in_base_class(self):
        e = E(one=1)
        e.three = 3
        f = F(one=2)
        f.four = 4
        assert not f <= e

    def test_attribute_order_matters(self):
        d1 = D(one=1, two=2)
        d2 = D(one=2, two=1)
        assert sorted([d1, d2]) == [d1, d2]

        g1 = G(one=1, two=2)
        g2 = G(one=2, two=1)
        assert sorted([g1, g2]) == [g2, g1]


class TestHash:

    def test_unhashable(self):
        # unhashable by default.
        with pytest.raises(TypeError):
            hash(A(one=1))

    def test_hashable(self):
        d = {}
        b12 = B(one=1, two=2)
        b34 = B(one=3, two=4)
        b12x = B(one=1, two=2, three=3)
        assert hash(b12) == hash(b12x)
        assert hash(b12) != hash(b34)


class TestAttrSpec:

    def test_single_attr(self):
        @essence('attr_one')
        class X(ThatBase): pass

        x = X(one=1)
        assert x.__essence__() == (1,)

    def test_multi_attr_in_string(self):
        @essence('attr_one attr_two')
        class X(ThatBase): pass

        x = X(one=1, two=2)
        assert x.__essence__() == (1, 2)
