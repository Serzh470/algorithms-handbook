""" 
Heap sort 
"""

def heapify(arr, n, i):
    """ Build heap """
    largest = i     # Initialize largest as root
    l = 2 * i + 1   # left = 2*i + 1
    r = 2 * i + 2   # right = 2*i + 2

    # is left leaf greater, than root
    if l < n and arr[i] < arr[l]:
        largest = l

    # is right leaf greater, than root
    if r < n and arr[largest] < arr[r]:
        largest = r

    # change root and leaf if needed
    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i] # swap

        # apply heapify to root
        heapify(arr, n, largest)


def heap_sort(arr):
    n = len(arr)

    # build max-heap.
    for i in range(n, -1, -1):
        heapify(arr, n, i)

    # extract elements
    for i in range(n-1, 0, -1):
        arr[i], arr[0] = arr[0], arr[i] # swap 
        heapify(arr, i, 0)

    return arr


def test_heap_sort():
    """ Tests """
    assert(heap_sort([3, 2, 5, 7, 3, 4, 7, 0, 3, 1, 3, 6]) == [0, 1, 2, 3, 3, 3, 3, 4, 5, 6, 7, 7])


if __name__ == '__main__':
    a = [3, 2, 5, 7, 3, 4, 7, 0, 3, 1, 3, 6]
    print('Choice sort for [3,2,5,7,3,4,7,0,3,1,3,6]: ', heap_sort(a))