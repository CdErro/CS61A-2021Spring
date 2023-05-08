def keep_ints(cond, n):
    """Print out all integers 1..i..n where cond(i) is true
    >>> def is_even(x):
    ...     # Even numbers have remainder 0 when divided by 2.
    ...     return x % 2 == 0
    >>> keep_ints(is_even, 5)
    2
    4
    """
    "*** YOUR CODE HERE ***"
    for i in range(1, n + 1):
        if cond(i):
            print(i)


def make_keeper(n):
    """Returns a function which takes one parameter cond and prints out all integers 1..i..n where calling cond(i) returns True.
        >>> def is_even(x):
        ...     # Even numbers have remainder 0 when divided by 2.
        ...     return x % 2 == 0
        >>> make_keeper(5)(is_even)
        2
        4
    """
    "*** YOUR CODE HERE ***"

    def pritfunc(cond):
        for i in range(1, n + 1):
            if cond(i):
                print(i)

    return pritfunc


def curry2():
    """
    >>> make_adder = curry2()(lambda x, y: x + y)
    >>> add_three = make_adder(3)
    >>> add_four = make_adder(4)
    >>> five = add_three(2)
    >>> five
    5
    >>> add_four(2)
    6
    """
    return lambda h: lambda x: lambda y: h(x, y)


def make_keeper_redux(n):# 测试用例里输出函数信息可能会不一样，例如<function make_keeper_redux.<locals>.do_keep at 0x000001EA38DEDA68>，下面几个函数也类似，结果相同就行
    """Returns a function. This function takes one parameter <cond> and prints out
       all integers 1..i..n where calling cond(i) returns True. The returned
       function returns another function with the exact same behavior.

        >>> def multiple_of_4(x):
        ...     return x % 4 == 0
        >>> def ends_with_1(x):
        ...     return x % 10 == 1
        >>> k = make_keeper_redux(11)(multiple_of_4)
        4
        8
        >>> k = k(ends_with_1)
        1
        11
        >>> k
        <function do_keep>
    """

    # Paste your code for make_keeper here!
    def do_keep(cond):
        for i in range(1, n + 1):
            if cond(i):
                print(i)
        return do_keep

    return do_keep


def print_delayed(x):
    """Return a new function. This new function, when called, will print out x and return another function with the same behavior.
    >>> f = print_delayed(1)
    >>> f = f(2)
    1
    >>> f = f(3)
    2
    >>> f = f(4)(5)
    3
    4
    >>> f("hi") # a function is returned
    5
    <function print_delayed.<locals>.delay_print at 0x0000013EB828F558>
    """

    def delay_print(y):
        print(x)
        return print_delayed(y)

    return delay_print


def print_n(n):
    """
    >>> f = print_n(2)
    >>> f = f("hi")
    hi
    >>> f = f("hello")
    hello
    >>> f = f("bye")
    done
    >>> g = print_n(1)
    >>> g("first")("second")("third")
    first
    done
    done
    <function inner_print>
    """

    def inner_print(x):
        if n == 0:
            print("done")
            return print_n(n)
        else:
            print(x)
            return print_n(n - 1)

    return inner_print
