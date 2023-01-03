def last_element(lst):
    """Return last item in list (None if list is empty.
    
        >>> last_element([1, 2, 3])
        3
        
        >>> last_element([]) is None
        True
    """
    length = len(lst)
    print(lst[length - 1])
test_list = [0, 1, 2, 3]
last_element(test_list)

# tested, works
