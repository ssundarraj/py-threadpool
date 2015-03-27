from utils import *
import requests


def printer(x):
    print x
    # print y
    print "Done"

t = Threadpool()
for i in range(100):
    j = ThreadJob(printer, ('hi'), None)
    t.add_job(j)
t.start()
t.finish()
