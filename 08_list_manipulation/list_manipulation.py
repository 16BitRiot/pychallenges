def list_manipulation(lst, command, location, value=None):
    length = len(lst)
    last = length - 1
    # start = lst[0]
    # print('last index', last)
    # print('string length', length)
    # print('start index', start)
    if command == 'remove' and (location == 'beginning' or 'end'):
        if location == 'end':
            last_element = lst.pop(last)
            return last_element
        if location == 'beginning':
            first_element = lst.pop(0)
            return first_element
    if command == 'add' and (location == 'beginning' or 'end'):
        if location == 'end':
            lst[length:length] = [value]
            return lst
        if location == 'beginning':
            lst.insert(0, value)
            return lst
    elif command not in ('remove', 'add') or location not in ('beginning', 'end'):
        return True
    """Mutate lst to add/remove from beginning or end.

    - lst: list of values
    - command: command, either "remove" or "add"
    - location: location to remove/add, either "beginning" or "end"
    - value: when adding, value to add

    remove: remove item at beginning or end, and return item removed

        >>> lst = [1, 2, 3]

        >>> list_manipulation(lst, 'remove', 'end')
        3

        >>> list_manipulation(lst, 'remove', 'beginning')
        1

        >>> lst
        [2]
        


    """
lst = [1, 2, 3]

# section 1 remove: completed and tested
# list_manipulation(lst, 'remove', 'end') 
# list_manipulation(lst, 'remove', 'beginning')
# print(lst)

# section 2 add: completed and tested
# list_manipulation(lst, 'add', 'beginning', 20)
# list_manipulation(lst, 'add', 'end', 30)
# print(lst)

# section 3 invalid commands: completed and tested
# list_manipulation(lst, 'foo', 'end')
# list_manipulation(lst, 'add', 'dunno')