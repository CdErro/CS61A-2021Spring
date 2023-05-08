import doctest


def get_k_run_starter(n, k):
    """
    >>> get_k_run_starter(123444345, 0) # example from description
    3
    >>> get_k_run_starter(123444345, 1)
    4
    >>> get_k_run_starter(123444345, 2)
    4
    >>> get_k_run_starter(123444345, 3)
    1
    >>> get_k_run_starter(123412341234, 1)
    1
    >>> get_k_run_starter(1234234534564567, 0)
    4
    >>> get_k_run_starter(1234234534564567, 1)
    3
    >>> get_k_run_starter(1234234534564567, 2)
    2
    """
    i = 0
    string = str(n)
    j = len(string) - 1
    while i <= k:
        while j >= 0:
            if string[j] > string[j - 1]:
                j -= 1
                continue
            else:
                if i == k:
                    return eval(string[j])
                else:
                    j -= 1
                    break
        i += 1


if __name__ == "__main__":
    doctest.testmod(verbose=True)
    '''get_k_run_starter(123444345,2)'''
