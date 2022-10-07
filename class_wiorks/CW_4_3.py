from datetime import datetime as dt
DB = {}

#что бы записывалось в файл .csv .json .txt отпарвить на e-male

def logger(f):
    def wraper(*args, **kwargs):
        start = dt.now()
        result = f(*args, **kwargs)
        DB[f.__name__] = start.strftime("%Y-%m-%d %H:%M:%S")
        return result
    return wraper


@logger
def foo():
    pass


@logger
def foo1():
    pass


@logger
def foo2():
    pass


@logger
def foo3():
    pass


foo1()
foo2()
foo3()
foo()



print(DB)
# {'foo1': "13:00", 'foo2':''}