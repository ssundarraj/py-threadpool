from utils import *
import requests


def printer(x, test=None):
    print x
    print test
    print "Done"

t = threadpool()
for i in range(100):
    j = thread_job(printer, ('formal'), {'test':'keyword'})
    t.add_job(j)
t.start()
t.finish()
