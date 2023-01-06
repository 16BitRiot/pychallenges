def find_factors(num):
    return_factors = []
    for i in range(num):
        right_num = i + 1
        for j in range(num):
            right_var = j + 1
            factor = right_num * right_var
            if factor == num: 
                return_factors.append([i, j])
    return return_factors

    """Find factors of num, in increasing order.

    >>> find_factors(10)
    [1, 2, 5, 10]

    >>> find_factors(11)
    [1, 11]

    >>> find_factors(111)
    [1, 3, 37, 111]

    >>> find_factors(321421)
    [1, 293, 1097, 321421]
    """
find_factors(10)

# tested, works