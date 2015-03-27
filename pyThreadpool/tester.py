from utils import *
import requests
from thread_job import thread_job
from threadpool import threadpool

def printer(x, y, testx=None, testy=None):
    print x, y, testx, testy
    print "Done"

t = threadpool()
for i in range(100):
    j = thread_job(printer, ('formalx', 'formaly'), {'testx': 'keywordx', 'testy': 'keywordy'})
    t.add_job(j)
t.start()
t.finish()
