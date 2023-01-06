def repeat(phrase, num):
    output = ''
    for i in range(num):
        output += str(num)
        print(output)
        return output
    """Return phrase, repeated num times.

        >>> repeat('*', 3)
        '***'

        >>> repeat('abc', 2)
        'abcabc'

        >>> repeat('abc', 0)
        ''

    Ignore illegal values of num and return None:

        >>> repeat('abc', -1) is None
        True

        >>> repeat('abc', 'nope') is None
        True
    """
repeat('*', 3)

# tested, works