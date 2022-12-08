def square_and_remove_positive(lst):
    '''Given a list of numbers, write a function that returns a new list where all the numbers are squared and all the positive numbers are removed.
    
    Args:
        lst (list): list of numbers.
    
    Returns:
        list: list of all non-negative numbers ared squared.
    '''
    ls = []
    for i in range(len(lst)):
        if 0 > lst[i]:
            lst[i] = lst[i] ** 2
            ls.append(lst[i])
    return ls
print(square_and_remove_positive([1, -2, 3, -4, 5]))