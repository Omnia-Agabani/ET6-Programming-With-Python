def mystery_8(a, b):
    """ 
    The function is giving a list of b in a
    
    parameters: 
    a: is a string or list
    b is a string
    
    Returns:
    list of b in a
    """
    
    assert not isinstance(a , int), "a should not be an int"
    assert isinstance(b , str), "b should be a string"
    c = []
    while a:
        if b in a[0]:
            c.append(a[0])
        a = a[1:]
    return c
