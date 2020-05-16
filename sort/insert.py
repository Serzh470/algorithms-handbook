""" 
Insert sort 
O(n**2)
"""

def insert_sort(a):
    n = len(a)
    for top in range(1, n):
        k = top
        while k > 0 and a[k-1] > a[k]:
            a[k], a[k-1] = a[k-1], a[k]
            k -= 1

    return a


def test_insert_sort():
    """ Tests """
    assert(insert_sort([3, 2, 5, 7, 3, 4, 7, 0, 3, 1, 3, 6]) == [0, 1, 2, 3, 3, 3, 3, 4, 5, 6, 7, 7])


if __name__ == '__main__':
    print('Insert sort for [3,2,5,7,3,4,7,0,3,1,3,6]: ', insert_sort([3, 2, 5, 7, 3, 4, 7, 0, 3, 1, 3, 6]))