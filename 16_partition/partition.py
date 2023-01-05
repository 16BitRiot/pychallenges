
def is_even(num):
    return num % 2 == 0

def is_string(el):
    return isinstance(el, str)

def partition(lst, fn):

    ab_list = [[], []]

    for x in lst:
        if fn(x):
            ab_list[0].append(x)
        else:
            ab_list[1].append(x)
    print(ab_list)

    """Partition lst by predicate.
     
     - lst: list of items
     - fn: function that returns True or False
     
     Returns new list: [a, b], where `a` are items that passed fn test,
     and `b` are items that failed fn test.

        >>> def is_even(num):
        ...     return num % 2 == 0
        
        >>> def is_string(el):
        ...     return isinstance(el, str)
        
        >>> partition([1, 2, 3, 4], is_even)
        [[2, 4], [1, 3]]
        
        >>> partition(["hi", None, 6, "bye"], is_string)
        [['hi', 'bye'], [None, 6]]
    """

partition([1, 2, 3, 4], is_even)
partition(["hi", None, 6, "bye"], is_string)

# tested, works