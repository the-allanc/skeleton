from crookbook import described, essence
import six

@essence(['site', 'tld'])
@described(inner='for "{0.site}" [{0.tld}]')
class Webpage(object): pass

@described(inner='for "{0.site}" [{0.tld}]')
class MyWebpage(object):

    def __str__(self):
        return 'My Webpage'

def test_described_inner():
    wp = Webpage()
    wp.site = 'google'
    wp.tld = 'nl'

    assert repr(wp) == '<Webpage for "google" [nl]>'
    assert str(wp) == '<Webpage for "google" [nl]>'
    if six.PY2:
        assert unicode(wp) == '<Webpage for "google" [nl]>'

def test_described_inner_with_explicit_str():
    wp = MyWebpage()
    wp.site = 'google'
    wp.tld = 'nl'

    assert repr(wp) == '<MyWebpage for "google" [nl]>'
    assert str(wp) == 'My Webpage'
    if six.PY2:
        assert unicode(wp) == 'My Webpage'
