import SimplePool
from nose.tools import eq_

t = SimplePool.ThreadPool()


def printer(x, y, testx=None, testy=None):
    print(x, y, testx, testy)
    # print "Done"
    a = {}
    # print a['b']
    eq_(x, 'formalx')
    eq_(y, 'formaly')
    eq_(testx, 'keywordx')
    eq_(testy, 'keywordy')
    return True


def test_intern():
    for i in range(100):
        args = ('formalx', 'formaly')
        kwargs = {'testx': 'keywordx', 'testy': 'keywordy'}
        j = SimplePool.ThreadJob(printer, args, kwargs)
        t.add_job(j)
    t.start()
    print(t.is_active)
    t.finish()

test_intern()
