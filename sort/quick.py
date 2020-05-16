""" 
Quicksort (Hoare)
Select barrier element
Compare all elements in list with barrier and divide list on 3 part:
    - less than barrier
    - equal barrier
    - greater than barrier
Merge lists
"""

def quicksort(a):
    if len(a) <= 1:
        return
    
    barrier = a[0]

    left = []
    middle = []
    right = []

    for x in a:
        if x < barrier:
            left.append(x)
        elif x == barrier:
            middle.append(x)
        else:
            right.append(x)

    quicksort(left)
    quicksort(right)

    k = 0
    for x in left + middle + right:
        a[k] = x
        k += 1

    return a


def test_quicksort():
    """ Tests """
    assert(quicksort([3, 2, 5, 7, 3, 4, 7, 0, 3, 1, 3, 6]) == [0, 1, 2, 3, 3, 3, 3, 4, 5, 6, 7, 7])


if __name__ == '__main__':
    print('Quick (Hoare) sort for [3,2,5,7,3,4,7,0,3,1,3,6]: ', quicksort([3, 2, 5, 7, 3, 4, 7, 0, 3, 1, 3, 6]))