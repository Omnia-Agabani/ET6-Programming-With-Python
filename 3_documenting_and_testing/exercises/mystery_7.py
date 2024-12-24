def mystery_7(a, b):
    """This function filters a list by searching for a substring within each element. It takes two parameters:

a: list or string to search through
b: substring to search for

It returns a new list containing only elements from a that include b as a substring.
    """
    assert not isinstance(a , int), "a should be an int"
    assert not isinstance(b , int), "b should be an int"
    c = []
    for d in a:
        if b in d:
            c.append(d)
    return c
