class thread_job:
    exec_function = None
    exeption = False
    callback = None  # Yet to be done
    args = []
    kwargs = {}

    def __init__(self, exec_function, args, kwds):
        self.exec_function = exec_function
        if type(args) == str or args == 0:
            self.args = (args,)
            self.args = (args,)
        else:
            self.args = (args) or []
        self.kwargs = kwds or {}

    def execute(self):
        self.exec_function(*self.args, **self.kwargs)
