def fibonacci(n):
    """Return the `n` th fibonacci number, for the positive `n` the number."""
    if 0 <= n <= 1:
        return n
    else:
        n = n+n
        print(n)

fibonacci(9)