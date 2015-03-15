import Queue
import threading


class ThreadPool:
    nhreads = 0
    q_size = 0
    job_q = Queue.Queue()
    threads = []
    total_jobs = 0

    def __init__(self, nthreads=10, q_size=0):
        self.nthreads = nthreads
        self.q_size = q_size

    def start(self):
        for i in range(self.nthreads):
            t = threading.Thread(target=self.worker)
            self.threads.append(t)
            t.start()
        return True

    def worker(self):
        while self.job_q.qsize():
            exec_function, args = self.job_q.get()
            if args:
                exec_function(args)
            else:
                exec_function()
            self.job_q.task_done()
        return True

    def add_job(self, exec_function, args=None):
        self.job_q.put((exec_function, args))
        self.total_jobs += 1
        return True

    def finish(self):
        self.job_q.join()
        return True

    def unfinished_tasks(self):
        return self.job_q.qsize()

    def finished_tasks(self):
        return self.total_jobs - self.job_q.qsize()
