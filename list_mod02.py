def remove_even(lst):
    '''Given a list of numbers, write a function that returns a new list where all the even numbers are removed.
    
    Args:
        lst (list): list of numbers.
        
    Returns:
        list: list without even numbers.
    '''
    i = 0
    ls = []
    for i in lst:
        if i % 2 == 0:
            ls.append(i)
    return ls
print(remove_even([1,2,3,4,5,6,7,8]))