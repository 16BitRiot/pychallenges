def flip_case(phrase, to_swap):
    updated_phrase = ''
    check_case = to_swap.isupper()
    print(check_case)
    for letter in phrase:
        if letter != to_swap:
            updated_phrase = updated_phrase + letter
        if letter == to_swap:
            if letter.isupper():
                print(letter, 'before')
                letter = letter.lower()
                updated_phrase = updated_phrase + letter
                print(letter, 'after')
            if letter.isupper() == False:
                letter = letter.upper()
                updated_phrase = updated_phrase + letter
    print(updated_phrase)
    """Flip [to_swap] case each time it appears in phrase.

        >>> flip_case('Aaaahhh', 'a')
        'aAAAhhh'

        >>> flip_case('Aaaahhh', 'A')
        'aAAAhhh'

        >>> flip_case('Aaaahhh', 'h')
        'AaaaHHH'

    """
flip_case('Aaaahhh', 'A')
flip_case('Aaaahhh', 'a')
flip_case('Aaaahhh', 'h')

# tested * works