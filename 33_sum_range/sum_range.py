nums = [1, 2, 3, 4]

def sum_range(nums, start=0, end=None):
    nums_length = len(nums)
    sum = 0
    if end is None:
        end = nums_length
    elif end > nums_length:
        end = nums_length
    else:
        end = end + 1
    for num in nums[start:end]:
        sum += num
    print(sum)
    """Return sum of numbers from start...end.

    - start: where to start (if not provided, start at list start)
    - end: where to stop (include this index) (if not provided, go through end)

        >>> nums = [1, 2, 3, 4]

        >>> sum_range(nums)
        10

        >>> sum_range(nums, 1)
        9

        >>> sum_range(nums, end=2)
        6

        >>> sum_range(nums, 1, 3)
        9

    If end is after end of list, just go to end of list:

        >>> sum_range(nums, 1, 99)
        9
    """
sum_range(nums)
sum_range(nums, 1)
sum_range(nums, end=2)
sum_range(nums, 1, 3)
sum_range(nums, 1, 99)

# tested, works