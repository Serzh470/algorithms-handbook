""" Mean of list  """
from functools import reduce

def mean_list(arr):
    """ Calculate mean of list """
    if not isinstance(arr, list):
        return 'Use only list with numbers for this function'

    if not len(arr):
        return None

    m = reduce(lambda x,y: x + y, arr, 0) / len(arr)
    return m


def test_sum_list():
    """ Tests """
    assert(mean_list([]) == None)
    assert(mean_list([3, 4, 5]) == 4)


if __name__ == '__main__':
    print('Count of list elenemts [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]: ', mean_list([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]))
