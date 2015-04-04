# py-threadpool
Thread pool library for Humans.

![Build Status](https://travis-ci.org/srirams6/py-threadpool.svg)
[![Coverage Status](https://coveralls.io/repos/srirams6/py-threadpool/badge.svg?branch=coverage)](https://coveralls.io/r/srirams6/py-threadpool?branch=coverage)

## Installation

#### Using `pip`
`pip install pyThreadpool` (Not supported yet)

or to get the source via pip, use

`pip install -e git+https://github.com/srirams6/py-threadpool.git#egg=pyThreadpool`

#### From source

* Clone from Github.
* Execute `python setup.py install`


## Usage

Basic usage is shown here.

```py
import pyThreadpool

# Function to be executed.
def printer(x, y, testx=None, testy=None):
    print x, y, testx, testy
    print "Done"

t = pyThreadpool.threadpool()

# Adding the same function 100 times
for i in range(100):
    args = ('formalx', 'formaly')
    kwargs = {'testx': 'keywordx', 'testy': 'keywordy'}
    j = pyThreadpool.thread_job(printer, args, kwargs)  # Create a thread_job object.
    t.add_job(j)
t.start()
t.finish()
```

## Contribute

If you want to add features, or improve anything feel free to send a pull request. If you have any issues, open an issue.

## Todo

* Putting results in `result_q` and handling the results
* Handling exceptions in the function call
