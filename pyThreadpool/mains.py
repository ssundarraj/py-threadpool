from utils import *
import requests


def printer():
    requests.get('http://google.com')
    print "Done"

t = ThreadPool()
for i in range(10):
    t.add_job(printer, None)
t.start()
t.finish()
