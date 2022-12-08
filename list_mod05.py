def square(lst):
    '''Given a list of numbers, write a function that returns a new list where all the numbers are squared.
    
    Args:
        lst (list): list of numbers.
        
    Returns:
        list: list of all numbers are squared.
    '''
    for i in range(len(lst)):
        lst[i] = lst[i] ** 2
    return lst

print(square([3,6,9]))