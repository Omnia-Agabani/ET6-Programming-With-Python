def mystery_9(a):
    """ 
    The function is sorting a given list
    
    parameters:
    a: list
    
    Return:
    sorted list
    """
    assert isinstance(a , list), "a should be a list"
    b = len(a)
    for c in range(b):
        for d in range(0, b - c - 1):
            if a[d] > a[d + 1]:
                a[d], a[d + 1] = a[d + 1], a[d]
    return a
