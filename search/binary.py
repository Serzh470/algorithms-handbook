""" 
Binary search in list.
List must be sorted.
speed - O(log2N)
"""

def binary_search(a, key):
    """ 
    a - sorted list 
    key - value for search
    returs: index or None
    """
    left = 0
    right = len(a)
    while left < right:
        middle = (left + right) // 2
        if key < a[middle]:
            right = middle
        elif key > a[middle]:
            left = middle + 1
        else:
            return middle
    return None


def test_binary_search():
    """ Tests """
    assert(binary_search([1, 2, 3, 4, 5, 6, 7, 8], 4) == 3)


if __name__ == '__main__':
    print('Binary search of 8 in list [1, 2, 3, 4, 5, 6, 7, 8]. Index is ', binary_search([1, 2, 3, 4, 5, 6, 7, 8], 8))
