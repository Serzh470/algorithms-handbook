""" Sieve of Eratosthenes """

def eratosthen(max):
    """ Generate initial list with values up to max. Then replace not prime nunmbers with 0 and filter they """
    all = list(range(0, max + 1))
    # exclude 1 as not prime number
    all[1] = 0

    i = 2
    while i < max:
        if all[i] != 0:
            j = i + i
            while j <= max:
                all[j] = 0
                j = j + i
        i += 1

    # collapse to unique values
    numbers = set(all)
    numbers.remove(0)

    return numbers



def test_eratosthen():
    """ Tests """
    assert(eratosthen(30) == {2, 3, 5, 7, 11, 13, 17, 19, 23, 29})



if __name__ == '__main__':
    print('Prime numbers for range from 2 to 100 are: ', eratosthen(100))
