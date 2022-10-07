from datetime import datetime as dt


def timer(funk):
    def wrapper(*args, **kwargs):
        start = dt.now()
        funk(*args, **kwargs)
        return start
    return wrapper


@timer
def count(n: int):
    while n < 10**8:
        n += 1
    return n




data_types_of_python = {
    "int": int,
    "str": str,
    "float": float,
    "bool": bool,
    "list": list,
    "dict": dict,
}
#try to solve more tasks on this topic
def only_chosen_types(lst: list):
    def wrapper_func(func):
        def wraper_args(*func_args, **func_kwargs):
            result = func(*func_args, **func_kwargs)
            dct = {val: result[val] for val in lst}
            return dct
        return wraper_args
    return wrapper_func


@only_chosen_types(["float", "int"])
def print_dict(d: dict) -> dict:
    return d

print(print_dict(data_types_of_python))
a = only_chosen_types(["float", "int", "str"])(print_dict)(data_types_of_python)
print(print_dict(data_types_of_python))
print(a)