def mystery_4(a):
    """
    The function is bring a list count till the given number
    

    Parameter:
        a (int): max number to count

    Returns:
        list: count till the max number
    """
    assert type(a) is int, "a should be an int "
    b = []

    c = 0
    while len(b) < a:
        b.append(c)
        c = c + 1

    return b
