""" 
Choice sort 
O(n**2)
"""

def choice_sort(a):
    n = len(a)
    for pos in range(0, n - 1):
        for k in range(pos + 1, n):
            if a[k] < a[pos]:
                a[k], a[pos] = a[pos], a[k]
    return a


def test_choice_sort():
    """ Tests """
    assert(choice_sort([3, 2, 5, 7, 3, 4, 7, 0, 3, 1, 3, 6]) == [0, 1, 2, 3, 3, 3, 3, 4, 5, 6, 7, 7])


if __name__ == '__main__':
    print('Choice sort for [3,2,5,7,3,4,7,0,3,1,3,6]: ', choice_sort([3, 2, 5, 7, 3, 4, 7, 0, 3, 1, 3, 6]))