# py-threadpool
Thread pool library for Humans.

## Installation

#### Using `pip`
`pip install pyThreadpool` (Not supported yet)

#### From source

* Clone from Github.
* Execute `python setup.py install`


## Usage

Basic usage is shown here.

```py
import pyThreadpool
import requests

def printer():
    requests.get('http://google.com')
    print "Done"

t = pyThreadPool.ThreadPool()
for i in range(10):
    t.add_job(printer, None)
t.start()
t.finish()
```

## Contribute

If you want to add features, or improve anything feel free to send a pull request. If you have any issues, open an issue.
