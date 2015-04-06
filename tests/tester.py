import ThreadPool


def printer(x, y, testx=None, testy=None):
    # print x, y, testx, testy
    # print "Done"
    a = {}
    # print a['b']
    return True

t = ThreadPool.ThreadPool()
for i in range(100):
    args = ('formalx', 'formaly')
    kwargs = {'testx': 'keywordx', 'testy': 'keywordy'}
    j = ThreadPool.ThreadJob(printer, args, kwargs)
    t.add_job(j)
t.start()
print(t.is_active)
t.finish()
print(t.is_active)
