def mystery_5(a, b):
    """ 
    The function sort the givin list
    and add the other list
    
    Parameters:
    a (list): need to be sort
    b (list): the fixed list
    
    Return:
    list: the second list with the first list sorted
    
    """
    assert type(a) is list, "a should be a list "
    assert type(b) is list, "b should be a list "

    while a:
        c = min(a)
        a.remove(c)
        b.append(c)
    return b
