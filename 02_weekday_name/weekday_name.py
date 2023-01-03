def weekday_name(day_of_week):
    days = {
        1: "Sunday", 
        2: "Monday",
        3: "Tuesday",
        4: "Wednesday",
        5: "Thursday",
        6: "Friday",
        7: "Saturday",
    }
    for i in range(1, 8):
        if day_of_week == i:
            print(days[i])
    if day_of_week == 0 or day_of_week >= 9:
        return None
    """Return name of weekday.
    
        >>> weekday_name(1)
        'Sunday'
        
        >>> weekday_name(7)
        'Saturday'
        
    For days not between 1 and 7, return None
    
        >>> weekday_name(9)
        >>> weekday_name(0)
    """
print(weekday_name(2))
print(weekday_name(0))
print(weekday_name(6))

# tested works