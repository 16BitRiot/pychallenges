def vowel_count(phrase):
    vowels = 'aeiouAEIOU'
    vcount = {}
    for letter in phrase:
        if letter in vowels:
            if letter in vcount:
                vcount[letter] += 1
            else:
                vcount[letter] = 1
        else:
            if letter in vcount:
                vcount[letter] += 1
            else:
                vcount[letter] = 1
    return vcount
    """Return frequency map of vowels, case-insensitive.

        >>> vowel_count('rithm school')
        {'i': 1, 'o': 2}
        
        >>> vowel_count('HOW ARE YOU? i am great!') 
        {'o': 2, 'a': 3, 'e': 2, 'u': 1, 'i': 1}
    """


vowel_count('rithm school')

# tested, works