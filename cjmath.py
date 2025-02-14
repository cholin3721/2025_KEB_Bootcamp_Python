def cj_abs(n) -> int :
    """
    :param n:
    :return: absolute value
    """

    if n < 0:
        return -n
    else :
        return n

def cj_fibonacci_recursion(n) -> int :
    """
    fibonacci number
    :param n:
    :return:
    """
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    else :
        return cj_fibonacci_recursion(n-1) + cj_fibonacci_recursion(n-2)

def cj_Fibonacci3(n) :
    a, b = 0, 1
    for i in range(n) :
        a, b = b, b+a
    return a
