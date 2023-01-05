def list_check(lst):
    for ck in lst:
        check = isinstance(ck, list)
        print(check)
        if check == False:
            return False
    return True
    """Are all items in lst a list?

        >>> list_check([[1], [2, 3]])
        True

        >>> list_check([[1], "nope"])
        False
    """
list_check([[1], [2, 3]])

# tested, works