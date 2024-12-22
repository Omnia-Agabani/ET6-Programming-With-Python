"""
    The function is check the length of the input
    
    Parameter:
    a value we want to check it's length
    
    Return:
    The length of the input    
    
    
    """
def mystery_2(a):
    assert type(a) is not int, "object of type int has no len() "
    if len(a) == 0:
        return None

    return len(a)
