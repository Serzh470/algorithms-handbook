""" Cal sum for list of numbers """
from functools import reduce

def sum_list(arr):
    """ Sum of all element in list """
    if not isinstance(arr, list):
        return 'Use only list with numbers for this function'

    s = reduce(lambda x,y: x + y, arr, 0)
    return s


def test_sum_list():
    """ Simple tests """
    assert(sum_list([]) == 0)
    assert(sum_list([3, 3, 3]) == 9)
    assert(sum_list('test') == 'Use only list with numbers for this function')


if __name__ == '__main__':
    print('Sum of list [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]: ', sum_list([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]))
