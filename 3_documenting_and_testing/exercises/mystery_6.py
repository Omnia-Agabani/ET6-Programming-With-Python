def mystery_6(a, b):
    """The function creates 'a' list of a sequential numbers, starting with 'b'

    Parameters:
        a (int): length
        b (int): the begging

    Return:
        List: 'a' sequential numbers, starting with b.
    """
    assert isinstance(a , int), "a should be an int"
    assert isinstance(b , int), "b should be an int"
    if a == 0:
        return []

    c = []
    while len(c) < a:
        c.append(b)
        b = b + 1

    return c
