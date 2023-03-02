def fibonacci(n):
    """
    an intuitive version of fibonacci
    """
    global number_fib_calls
    if 'number_fib_calls' not in globals():
        number_fib_calls = 0
    number_fib_calls += 1
    if n == 0:
        return 1
    elif n == 1:
        return 1
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)


known = {0: 1, 1: 1}


def fib_efficient(n):
    """
    a "memori version of fibonacci
    """
    global number_fib_calls
    if 'number_fib_calls' not in globals():
        number_fib_calls = 0
    number_fib_calls += 1
    if n in known:
        return known[n]
    else:
        ans = fib_efficient(n - 1) + fib_efficient(n - 2)
        known[n] = ans
        return ans


def main():
    fib_args = 10
    global number_fib_calls
    number_fib_calls = 0
    print(f'The {fib_args}th Fibonacci number is {fibonacci(fib_args)}.')
    print('# of function calls:', number_fib_calls)

    number_fib_calls = 0
    print(f'The {fib_args}th Fibonacci number is {fib_efficient(fib_args)}.')
    print('# of function calls:', number_fib_calls)


if __name__ == '__main__':
    main()
