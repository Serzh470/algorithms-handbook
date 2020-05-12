""" Max element in list  """

def max_list(arr):
    """ Count elements in list """
    if not isinstance(arr, list):
        return 'Use only list with numbers for this function'

    if not len(arr):
        return None

    m = arr[0]
    for i in arr:
        m = i if i > m else m
    return m


def test_max_list():
    """ Tests """
    assert(max_list([]) == None)
    assert(max_list([3, 4, 5]) == 5)


if __name__ == '__main__':
    print('Count of list elenemts [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]: ', max_list([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]))
