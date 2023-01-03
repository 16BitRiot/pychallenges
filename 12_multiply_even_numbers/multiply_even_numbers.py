def multiply_even_numbers(nums):
    return_total = 1
    def even_checker(x):
        if x % 2 == 0:
            return True
        else:
            return False
    for num in nums:
        if even_checker(num) == True:
            return_total = return_total * num
    print(return_total)
    return return_total
    """Multiply the even numbers.
    
        >>> multiply_even_numbers([2, 3, 4, 5, 6])
        48
        
        >>> multiply_even_numbers([3, 4, 5])
        4
        
    If there are no even numbers, return 1.
    
        >>> multiply_even_numbers([1, 3, 5])
        1
    """
 
multiply_even_numbers([2, 3, 4, 5, 6])
multiply_even_numbers([3, 4, 5])
multiply_even_numbers([1, 3, 5])

# tested, works