def square_and_remove_divisible_by_3(lst):
    '''Given a list of numbers, write a function that returns a new list where all the numbers are squared and all the numbers that are divisible by 3 are
    
    Args:
        lst (list): list of numbers.
    
    Returns:
        list: list of all numbers are not divisible by 3.
    '''
    ls = []
    for i in range(len(lst)):
        lst[i] = lst[i] ** 2
        ls.append(lst[i])
    i = 0
    while i < len(ls):
        if ls[i] % 3 == 0:
            ls.pop(i)
        i += 1
    return ls
print(square_and_remove_divisible_by_3([1, 2, 3, 4, 9, 5]))