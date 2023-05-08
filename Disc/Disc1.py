import doctest


def wears_jacket_with_if(temp, raining):
    """
    >>> wears_jacket_with_if(90, False)
    False
    >>> wears_jacket_with_if(40, False)
    True
    >>> wears_jacket_with_if(100, True)
    True
    """
    "*** YOUR CODE HERE ***"
    if temp < 60 or raining:
        return True
    else:
        return False


def wears_jacket(temp, raining):
    """
        >>> wears_jacket_with_if(90, False)
        False
        >>> wears_jacket_with_if(40, False)
        True
        >>> wears_jacket_with_if(100, True)
        True
        """
    "*** YOUR CODE HERE ***"
    return True if temp < 60 or raining else False


def is_prime(n):
    """
    >>> is_prime(10)
    False
    >>> is_prime(7)
    True
    """
    "*** YOUR CODE HERE ***"
    i = 2
    while i < n:
        if n % i == 0:
            return False
        else:
            i += 1
            continue
    return True


def fizzbuzz(n):
    """
    >>> result = fizzbuzz(16)
    1
    2
    fizz
    4
    buzz
    fizz
    7
    8
    fizz
    buzz
    11
    fizz
    13
    14
    fizzbuzz
    16
    >>> result == None
    True
    """
    "*** YOUR CODE HERE ***"
    i = 1
    while i <= n:
        if i % 3 == 0 and i % 5 == 0:
            print("fizzbuzz")
        elif i % 3 == 0:
            print("fizz")
        elif i % 5 == 0:
            print("buzz")
        else:
            print(i)
        i += 1
    return None


if __name__ == "__main__":
    doctest.testmod()
