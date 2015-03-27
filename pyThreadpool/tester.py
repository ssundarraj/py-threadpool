import threadpool

def printer(x, y, testx=None, testy=None):
    print x, y, testx, testy
    print "Done"

t = threadpool.threadpool()
for i in range(100):
    args = ('formalx', 'formaly')
    kwargs = {'testx': 'keywordx', 'testy': 'keywordy'}
    j = threadpool.thread_job(printer, args, kwargs)
    t.add_job(j)
t.start()
t.finish()
