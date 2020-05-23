""" Longest increasing subsequence """

def lis(a):
    F = [0] * len(a)
    for i in range(len(a)):
        for j in range(i):
            if a[j] < a[i] and F[j] > F[i]:
                F[i] = F[j]
        F[i] += 1

    m = max(F)

    return m


def test_lis():
    """ Tests """
    assert(lis([10, 22, 9, 33, 21, 50, 41, 60]) == 5)


if __name__ == '__main__':
    print('LIS of is ', lis([10, 22, 9, 33, 21, 50, 41, 60]))
