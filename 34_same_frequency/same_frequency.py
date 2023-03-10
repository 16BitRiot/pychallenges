from collections import Counter

def same_frequency(num1, num2):
    count1 = Counter(str(num1))
    count2 = Counter(str(num2))
    return count1 == count2

    """Do these nums have same frequencies of digits?
    
        >>> same_frequency(551122, 221515)
        True
        
        >>> same_frequency(321142, 3212215)
        False
        
        >>> same_frequency(1212, 2211)
        True
    """
same_frequency(551122, 221515)
same_frequency(321142, 3212215)
same_frequency(1212, 2211)

# tested, works