class thread_job:

    def __init__(self, exec_function, args=None, kwds=None):
        self.exception = False
        self.callback = None  # Yet to be done
        self.args = []
        self.kwargs = {}
        self.return_value = None
        self.exec_function = exec_function
        if type(args) == str or args == 0:
            self.args = (args,)
        else:
            self.args = (args) or []
        self.kwargs = kwds or {}

    def execute(self):
        try:
            self.return_value = self.exec_function(*self.args, **self.kwargs)
        except Exception as e:
            self.exception = e
