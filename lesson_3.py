from datetime import datetime


def execution_time(param):
    z = {
        'x': 'ADMIN',
        'y': 'USER'
    }

    def super_wrapper(func_name):
        def wrapper(*args, **kwargs):
            start = datetime.now()
            r = func_name(*args, **kwargs)
            stop = datetime.now()
            print(z[param])
            return r - 1
        return wrapper
    return super_wrapper


@execution_time('x')
def print_x(x):
    return x


@execution_time('y')
def print_y(y):
    return y


a = execution_time("y")(print_x)(5)


print(print_x(5))
print(print_y(5))