def square_and_remove_odd(lst):
    '''Given a list of numbers, write a function that returns a new list where all the numbers are squared and all the odd numbers are removed.
    
    Args:
        lst (list): list of numbers.
        
    Returns:
        list: list of all odd numbers are squared.
    '''
    list1 = []
    for i in range(len(lst)):
        lst[i] = lst[i] ** 2
        if lst[i] % 2 == 0:
            list1.append(lst[i])
    return list1
print(square_and_remove_odd([1,2,3,4,5]))