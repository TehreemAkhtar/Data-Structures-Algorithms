# def decorator(func):
#     def wrapper():
#         print("This is printed before the function is called")
#         func()
#         print("This is printed after the function is called")
#
#
# def say_hello():
#     print("Hello world")
#
#
# decorator(say_hello)

#
# def do_twice(func):
#     def wrapper(*args, **kwargs):
#         func(*args, **kwargs)
#         func(*args, **kwargs)
#     return wrapper
#
#
# @do_twice
# def say_hello(name):
#     print(f"Hello {name}")
#
#
# say_hello('Tehreem')


from functools import partial


def power(base, exponent):
    return base ** exponent


square = partial(power, 2)
cube = partial(power, 3)

print(square(3))
