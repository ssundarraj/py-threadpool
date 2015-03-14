import Queue
import threading

class ThreadPool:
	nhreads = 0
	q_size = 0
	job_q = Queue.Queue()
	threads = []
	
	def __init__(self, nthreads=10, q_size=0):
		self.nthreads = nthreads
		self.q_size = q_size

	def start():
		for i in range(nthreads):
			t = threading.Thread(target=worker)
			threads.append(t)
			t.start()

	def worker():
		pass