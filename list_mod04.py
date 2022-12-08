def remove_positive(lst):
    '''Given a list of numbers, write a function that returns a new list where all the positive numbers are removed.
    
    Args:
        lst (list): list of numbers.
        
    Returns:
        list: list without positive numbers.
    '''
    ls = []
    for i in lst:
        if i < 0:
            ls.append(i)
    return ls
print(remove_positive([1,2,3,4,5,-1,-2,-9]))