def mul(x, n):
    if n == 0:
        return 1
    else:
        return x * mul(x, n-1)
    