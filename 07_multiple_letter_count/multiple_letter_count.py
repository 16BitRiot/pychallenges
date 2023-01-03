def multiple_letter_count(phrase):
    """Return dict of {ltr: frequency} from phrase.

        >>> multiple_letter_count('yay')
        {'y': 2, 'a': 1}

        >>> multiple_letter_count('Yay')
        {'Y': 1, 'a': 1, 'y': 1}
    """
    letters = {}
    for let in phrase:
        if let in letters:
            letters[let] += 1
        else:
            letters[let] =1
    print(letters)
    return letters
multiple_letter_count('Yay')
multiple_letter_count('yay')

# tested, works