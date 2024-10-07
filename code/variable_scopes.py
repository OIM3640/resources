"""
LEGB
Local, Enclosing, Global, Built-in
"""

x = "global x"


# def f():
#     y = 'local y'
#     print(y)
#     print(x)
#
# f()
m = min([5, 1, 4, 2, 3])
print(m)


def f(z):
    y = "local y"
    print(z)


# f('local z')


def outer():
    # global x
    x = "outer x"

    def inner():
        nonlocal x
        x = "inner x"
        print(x)

    inner()
    print(x)


outer()
print(x)
