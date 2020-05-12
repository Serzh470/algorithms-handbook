""" Check if list is sorted """

def check_sort(a, ascending=True):
    flag = True
    # control order: ascending (positive numbers), descending (negative numbers)
    s = 2 * int(ascending) - 1
    for i in range(0, len(a) - 1):
        if s * a[i] > s * a[i + 1]:
            flag = False
            break

    return flag


def test_check_sort():
    """ Tests """
    assert(check_sort([1, 2, 3, 4, 5]) == True)


if __name__ == '__main__':
    print('Check if list [1, 2, 3, 4, 5] sorted ->', check_sort([1, 2, 3, 4, 5]))
    print('Check if list [1, 2, 3, 4, 0] sorted ->', check_sort([1, 2, 3, 4, 5]))