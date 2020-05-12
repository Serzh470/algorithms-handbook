""" Count elements in list  """

def count_list(arr):
    """ Count elements in list """
    c = len(arr)
    return c


def test_count_list():
    """ Tests """
    assert(count_list([]) == 0)
    assert(count_list([3, 3, 3]) == 3)


if __name__ == '__main__':
    print('Count of list elenemts [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]: ', count_list([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]))
