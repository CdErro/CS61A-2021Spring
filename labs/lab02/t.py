import doctest


def cycle(f1, f2, f3):
    """Returns a function that is itself a higher-order function.

    >>> def add1(x):
    ...     return x + 1
    >>> def times2(x):
    ...     return x * 2
    >>> def add3(x):
    ...     return x + 3
    >>> my_cycle = cycle(add1, times2, add3)
    >>> identity = my_cycle(0)
    >>> identity(5)
    5
    >>> add_one_then_double = my_cycle(2)
    >>> add_one_then_double(1)
    4
    >>> do_all_functions = my_cycle(3)
    >>> do_all_functions(2)
    9
    >>> do_more_than_a_cycle = my_cycle(4)
    >>> do_more_than_a_cycle(2)
    10
    >>> do_two_cycles = my_cycle(6)
    >>> do_two_cycles(1)
    19
    """
    "*** YOUR CODE HERE ***"

    def output(n):
        if n == 0:
            return lambda x: x
        else:
            g = lambda x: x
            for i in range(1, n + 1):
                flag = (i - 1) % 3
                if flag == 0:
                    f = lambda x: f1(g(x))
                elif flag == 1:
                    f = lambda x: f2(g(x))
                else:
                    f = lambda x: f3(g(x))
                g = f
            return g

    return output


def add1(x):
    return x + 1


def add2(x):
    return x + 2


def mul2(x):
    return x * 2


cycle1 = cycle(add1, add2, mul2)
fcycle0 = cycle1(0)
fcycle1 = cycle1(1)
fcycle2 = cycle1(2)
fcycle0(3)
fcycle1(3)
fcycle2(3)

