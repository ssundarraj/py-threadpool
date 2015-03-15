# py-threadpool
Thread pool library for Humans.

## Installation

#### Using `pip`
`pip install py_threadpool` (Not supported yet)

#### From source

* Clone from Github.
* Execute `python setup.py install`


## Usage

Basic usage is shown here.

```py
import py_threadpool as ThreadPool
import requests

def printer():
    requests.get('http://google.com')
    print "Done"

t = ThreadPool.ThreadPool()
for i in range(10):
    t.add_job(printer, None)
t.start()
t.finish()
```

## Contribute

If you want to add features, or improve anything feel free to send a pull request. If you have any issues, open an issue.
