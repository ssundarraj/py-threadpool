from utils import *

t = ThreadPool()
def printer():
    print "hello\n"

for i in range(10):
    t.add_job(printer, None)

t.start()