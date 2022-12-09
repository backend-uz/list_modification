def remove_max(lst):
    '''Given a list of numbers, write a function that returns a new list where all the maximum numbers are removed.
    
    Args:
        lst (list): list of numbers.
        
    Returns:
        list: list without maximum numbers.
    '''
    ls = []
    mx = 0

    for i in range(len(lst)):
        if lst[i] > mx:
            mx = lst[i]
    i = 0
    while i < len(lst):
        if lst[i] != mx:
            ls.append(lst[i])
        i += 1
    return ls
print(remove_max([1, 2, 3, 4, 5]))