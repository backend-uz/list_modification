def remove_negative(lst):
    '''Given a list of numbers, write a function that returns a new list where all the negative numbers are removed.
    
    Args:
        lst (list): list of numbers.
        
    Returns:
        list: list without negative numbers.
    '''
    ls = []
    for i in lst:
        if i > 0:
            ls.append(i)
    return ls
print(remove_negative([-1,-2,3,-4,6]))