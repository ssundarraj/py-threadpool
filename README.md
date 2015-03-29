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
