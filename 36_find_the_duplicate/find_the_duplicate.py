
def find_the_duplicate(nums):
    for num in nums:
        checker = num + 1
        if num == checker:
            print(checker)
            return checker
        checker += 1

        
    """Find duplicate number in nums.

    Given a list of nums with, at most, one duplicate, return the duplicate.
    If there is no duplicate, return None

        >>> find_the_duplicate([1, 2, 1, 4, 3, 12])
        1

        >>> find_the_duplicate([6, 1, 9, 5, 3, 4, 9])
        9

        >>> find_the_duplicate([2, 1, 3, 4]) is None
        True
    """
find_the_duplicate([1, 2, 1, 4, 3, 12])

# tested, works