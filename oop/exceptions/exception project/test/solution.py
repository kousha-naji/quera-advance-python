class ExceptionProxy(Exception):

    def __init__(self, msg, function):
        self.msg = msg
        self.function = function


def transform_exceptions(func_ls):
    func_have_exception = []
    for func in func_ls:
        try:
            func()
        except Exception as e:
            exception_obj = ExceptionProxy(msg=str(e), function=func)
            func_have_exception.append(exception_obj)
        else:
            exception_obj = ExceptionProxy(msg="ok!", function=func)
            func_have_exception.append(exception_obj)
    return func_have_exception


def f():
    return 1 / 0


def g():
    pass


exceptions = transform_exceptions([f, g])


for exception in exceptions:
    print(f"function name: {exception.function.__name__}")
    print(f"message: {exception.msg}")
