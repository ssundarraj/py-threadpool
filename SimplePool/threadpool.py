from .worker_thread import WorkerThread
try:
    import Queue
except ImportError:
    import queue as Queue


class ThreadPool(object):

    def __init__(self, nthreads=10):
        self.nthreads = 0
        self._q_size = 0
        self._job_q = Queue.Queue()
        self._result_q = Queue.Queue()
        self._total_jobs = 0
        self._threads = []
        self.is_active = 0
        self.nthreads = nthreads

    def __len__(self):
        return len(self._threads)

    def start(self):
        for i in range(self.nthreads):
            t = WorkerThread(self._job_q, self._result_q)
            self.is_active = True
            self._threads.append(t)
            t.start()
        return True

    def add_job(self, job):
        self._job_q.put(job)
        self._total_jobs += 1
        return True

    def finish(self):
        self._job_q.join()
        self.is_active = False
        return True

    def unfinished_tasks(self):
        return self._job_q.qsize()

    def finished_tasks(self):
        return self._total_jobs - self._job_q.qsize()
