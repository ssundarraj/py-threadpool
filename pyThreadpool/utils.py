import Queue
import threading


class Threadpool:
    _nhreads = 0
    _q_size = 0
    _job_q = Queue.Queue()
    _total_jobs = 0
    _threads = []

    def __init__(self, nthreads=10, q_size=0):
        self._nthreads = nthreads
        self._q_size = q_size

    def start(self):
        for i in range(self._nthreads):
            t = threading.Thread(target=self.worker)
            self._threads.append(t)
            t.start()
        return True

    def worker(self):
        while self._job_q.qsize():
            exec_function, args = self._job_q.get()
            if args:
                exec_function(args)
            else:
                exec_function()
            self._job_q.task_done()
        return True

    def add_job(self, exec_function, args=None):
        self._job_q.put((exec_function, args))
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


    def __init__(exec_function, args, kwargs):
        self.exec_function = exec_function
        self.args = args or []
        self.kwargs = kwargs or {}
