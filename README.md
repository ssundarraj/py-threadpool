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
import threadpool

def printer(x, y, testx=None, testy=None):
    print x, y, testx, testy
    print "Done"

t = threadpool.threadpool()
for i in range(100):
    args = ('formalx', 'formaly')
    kwargs = {'testx': 'keywordx', 'testy': 'keywordy'}
    j = threadpool.thread_job(printer, args, kwargs)
    t.add_job(j)
t.start()
t.finish()
```

## Contribute

If you want to add features, or improve anything feel free to send a pull request. If you have any issues, open an issue.
