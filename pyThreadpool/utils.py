import Queue
import threading


class Threadpool:
    _nhreads = 0
    _q_size = 0
    _job_q = Queue.Queue()
    _total_jobs = 0
    _threads = []

    def __init__(self, nthreads=10):
        self._nthreads = nthreads

    def start(self):
        for i in range(self._nthreads):
            t = threading.Thread(target=self.worker)
            self._threads.append(t)
            t.start()
        return True

    def worker(self):
        while self._job_q.qsize():
            try:
                job = self._job_q.get(None)
            except Queue.Empty:  # Exit the worker if Q empty
                return True
            job.execute()
            self._job_q.task_done()
        return True

    def add_job(self, job):
        self._job_q.put(job)
        self._total_jobs += 1
        return True

    def finish(self):
        self._job_q.join()
        return True

    def unfinished_tasks(self):
        return self._job_q.qsize()

    def finished_tasks(self):
        return self._total_jobs - self._job_q.qsize()


class ThreadJob:
    exec_function = None
    exeption = False
    callback = None  # Yet to be done
    args = []
    kwargs = {}

    def __init__(self, exec_function, args, kwds):
        self.exec_function = exec_function
        if type(args) == str:
            self.args = (args,)
        else:
            self.args = (args) or []
        self.kwargs = kwds or {}

    def execute(self):
        self.exec_function(*self.args, **self.kwargs)
