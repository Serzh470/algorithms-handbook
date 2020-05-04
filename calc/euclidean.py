""" Euclidean algorithm (greatest common divisor (GCD))  """

def euclidean(a, b):
    while a != 0 and b != 0:
        print(a, b)
        if a > b:
            a = a % b
        else:
            b = b % a


    gcd = a or b
    return gcd


def test_sum_list():
    """ Simple tests """
    assert(euclidean(30, 18) == 6)
    assert(euclidean(10, 10) == 10)
    assert(euclidean(0, 0) == 0)


if __name__ == '__main__':
    print('GCD for 30 and 18 is ', euclidean(30, 18))