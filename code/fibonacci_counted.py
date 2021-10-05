def fib(n):
    """
    an intuitive version of fibonacci
    """
    global number_fib_calls
    number_fib_calls += 1
    if n == 1:
        return 1
    elif n == 2:
        return 2
    else:
        return fib(n - 1) + fib(n - 2)


known = {1: 1, 2: 2}


def fib_efficient(n):
    """
    a "memori version of fibonacci
    """
    global number_fib_calls
    number_fib_calls += 1
    if n in known:
        return known[n]
    else:
        ans = fib_efficient(n - 1) + fib_efficient(n - 2)
        known[n] = ans
        return ans


number_fib_calls = 0
fib_args = 10

print(fib(fib_args))
print('function calls', number_fib_calls)

number_fib_calls = 0

print(fib_efficient(fib_args))
print('function calls', number_fib_calls)
