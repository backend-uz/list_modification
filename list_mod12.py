def remove_min(lst):
    '''Given a list of numbers, write a function that returns a new list where all the minimum numbers are removed.
    
    Args:
        lst (list): list of numbers.
        
    Returns:
        list: list wihout minimum numbers.
    '''
    mn = 0
    ls = []

    for i in range(len(lst)):
        if lst[i] < lst[1]:
            mn = lst[i]
    i = 0
    while i < len(lst):
        if lst[i] != mn:
            ls.append(lst[i])
        i += 1
    return ls
print(remove_min([2, 3, 4, 5]))