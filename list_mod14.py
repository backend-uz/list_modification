def replace_minimun_with_0(lst):
    """Given the list of numbers, Replace the mininum numbers in the list with 0.

    Args:
        lst (list): list of numbers
    Returns: 
        list: list minimum numbers are replaced with 0
    """
    mn = 0
    for i in range(len(lst)):
        if lst[i] < lst[1]:
            mn = lst[i]
    i = 0
    while i < len(lst):
        if lst[i] == mn:
            lst[i] = 0
        i += 1
    return lst
print(replace_minimun_with_0([1,2,3,4,5,6]))