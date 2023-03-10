def truncate(phrase, n):
    if n < 3:
        return "Truncation must be at least 3 characters."

    word_length = n - 3
    new_phrase = phrase
    if len(new_phrase) > word_length:
        new_phrase = new_phrase[:word_length] + "..."
    print(new_phrase)
    return new_phrase
    """Return truncated-at-n-chars version of  phrase.
    
    If the phrase is longer than, or the same size as, n make sure it ends with '...' and is no
    longer than n.
    
        >>> truncate("Hello World", 6)
        'Hel...'
        
        >>> truncate("Problem solving is the best!", 10)
        'Problem...'
        
        >>> truncate("Yo", 100)
        'Yo'
        
    The smallest legal value of n is 3; if less, return a message:
    
        >>> truncate('Cool', 1)
        'Truncation must be at least 3 characters.'

        >>> truncate("Woah", 4)
        'W...'

        >>> truncate("Woah", 3)
        '...'
    """
truncate("Hello World", 6)
truncate("Problem solving is the best!", 10)
truncate("Yo", 100)
truncate("Woah", 3)

# tested, works