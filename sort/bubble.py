""" 
Bubble sort 
O(n**2)
"""

def bubble_sort(a):
    n = len(a)
    for bypass in range(1, n):
        for k in range(0, n - bypass):
            if a[k] > a[k+1]:
                a[k], a[k+1] = a[k+1], a[k]
    return a


def test_bubble_sort():
    """ Tests """
    assert(bubble_sort([3, 2, 5, 7, 3, 4, 7, 0, 3, 1, 3, 6]) == [0, 1, 2, 3, 3, 3, 3, 4, 5, 6, 7, 7])


if __name__ == '__main__':
    print('Choice sort for [3,2,5,7,3,4,7,0,3,1,3,6]: ', bubble_sort([3, 2, 5, 7, 3, 4, 7, 0, 3, 1, 3, 6]))