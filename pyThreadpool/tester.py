from utils import *
import requests


def printer(x, y, testx=None, testy=None):
    print x,y,testx,testy
    print "Done"

t = threadpool()
for i in range(100):
    j = thread_job(printer, ('formalx', 'formaly'), {'testx':'keywordx', 'testy':'keywordy'})
    t.add_job(j)
t.start()
t.finish()
