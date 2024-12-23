def mystery_3(a, b):
    """
    The function send the minimum value
    or the summation incase they are equal
    

    Parameters:
    2 values from the same type
    
    Return:
    The minimum value or the summation incase they are equal
    """
    assert type(a) is type(b), "a and b are not the same type"  
    if a < b:
        return a
    elif a > b:
        return b
    else:
        return a + b
