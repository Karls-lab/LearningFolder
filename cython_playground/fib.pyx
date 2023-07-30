def fib(n):
    if n <= 1:
        return n

    fib_minus_2 = 0
    fib_minus_1 = 1
    fib_current = 0

    for _ in range(2, n+1):
        fib_current = fib_minus_2 + fib_minus_1
        fib_minus_2 = fib_minus_1
        fib_minus_1 = fib_current

    return fib_current