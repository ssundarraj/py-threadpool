from utils import *
import requests

t = ThreadPool()
def printer():
    requests.get('http://google.com')
    print "Done"

for i in range(10):
    t.add_job(printer, None)

t.start()
t.finish()