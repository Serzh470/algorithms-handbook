""" 
Mergesort 
Divide incoming list on parts, not more 1 elemets in list
Merge element on back recurrent move with sorting
"""

def merge(a, b):
    """ Merging 2 lists """
    i = 0
    k = 0
    c = []
    while i < len(a) and k < len(b):
        if a[i] <= b[k]:
            c.append(a[i])
            i += 1
        else:
            c.append(b[k])
            k += 1
             
    while i < len(a):
        c.append(a[i])
        i += 1

    while k < len(b):
        c.append(b[k])
        k += 1

    return c
        

def mergesort(a):
    """ Recurrent function for sorting list """
    if len(a) <= 1:
        return

    middle = len(a) // 2
    left = [a[i] for i in range(0, middle)]
    right = [a[i] for i in range(middle, len(a))]

    mergesort(left)
    mergesort(right)

    c = merge(left, right)

    for i in range(len(a)):
        a[i] = c[i]

    return a


def test_mergesort():
    """ Tests """
    assert(mergesort([3, 2, 5, 7, 3, 4, 7, 0, 3, 1, 3, 6]) == [0, 1, 2, 3, 3, 3, 3, 4, 5, 6, 7, 7])


if __name__ == '__main__':
    print('Merge sort for [3,2,5,7,3,4,7,0,3,1,3,6]: ', mergesort([3, 2, 5, 7, 3, 4, 7, 0, 3, 1, 3, 6]))