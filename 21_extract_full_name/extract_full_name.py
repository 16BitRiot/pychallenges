names = [
    {'first': 'Ada', 'last': 'Lovelace'},
    {'first': 'Grace', 'last': 'Hopper'},
]
def extract_full_names(people):
    full_names = []
    for num in people:
        full_names.append(num['first']+' '+num['last'])
    print(full_names)
    return full_names
    """Return list of names, extracting from first+last keys in people dicts.

    - people: list of dictionaries, each with 'first' and 'last' keys for
              first and last names

    Returns list of space-separated first and last names.

        >>> extract_full_names(names)
        ['Ada Lovelace', 'Grace Hopper']
    """
extract_full_names(names)

# tested, works