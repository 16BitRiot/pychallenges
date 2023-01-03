def is_palindrome(phrase):
    updated_word = phrase.replace(" ", "")
    updated_word = updated_word.lower()
    if updated_word == updated_word[::-1]:
        return True
    else:
        return False
    """Is phrase a palindrome?

    Return True/False if phrase is a palindrome (same read backwards and
    forwards).

        >>> is_palindrome('tacocat')
        True

        >>> is_palindrome('noon')
        True

        >>> is_palindrome('robert')
        False

    Should ignore capitalization/spaces when deciding:

        >>> is_palindrome('taco cat')
        True

        >>> is_palindrome('Noon')
        True
    """


# all tested/all work
# is_palindrome('tacocat')
# is_palindrome('noon')
# is_palindrome('robert')
# is_palindrome('taco cat')
# is_palindrome('Noon')
