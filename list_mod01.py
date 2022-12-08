def remove_odd(lst):
    '''Given a list of numbers, write a function that returns a new list where all the odd numbers are removed.

    Args:
        lst (list): a list of number.
    
    Returns:
        list: list without odd numbers.
    '''
    i = 0
    ls = []
    while i < len(lst):
        if lst[i] % 2 != 0:
            ls.append(lst[i])
        i += 1
    return ls
print(remove_odd([1,2,3,4,5,6,7]))