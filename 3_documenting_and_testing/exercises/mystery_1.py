"""
    The function add two value from the same type
        
    Parameters:
    a,b: 2 values from the same type
    
    Return:
    The summation of the 2 value
    
    
"""

def mystery_1(a,b):
    assert type(a) is type(b), "a and b are not the same type"  
    return a + b
