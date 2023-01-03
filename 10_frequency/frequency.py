def frequency(lst, search_term):
    counter = 0
    for num in lst:
        if num == search_term:
            counter += 1
    return counter
    """Return frequency of term in lst.
    
        >>> frequency([1, 4, 3, 4, 4], 4)
        3
        
        >>> frequency([1, 4, 3], 7)
        0
    """

# tested examples, works
frequency([1, 4, 3, 4, 4], 4)
frequency([1, 4, 3], 7)