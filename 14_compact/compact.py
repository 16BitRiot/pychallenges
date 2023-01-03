def compact(lst):
    updated_lst = []
    for item in lst:
        if bool(item) == True:
            updated_lst.append(item)

    print(updated_lst)
    return updated_lst
    """Return a copy of lst with non-true elements removed.

        >>> compact([0, 1, 2, '', [], False, (), None, 'All done'])
        [1, 2, 'All done']
    """

compact([0, 1, 2, '', [], False, (), None, 'All done'])

# tested, works