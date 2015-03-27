from utils import *
import requests


def printer(x, test=None):
    print x
    print test
    print "Done"

t = Threadpool()
for i in range(100):
    j = ThreadJob(printer, ('formal'), {'test':'keyword'})
    t.add_job(j)
t.start()
t.finish()
