""" Longest increasing subsequence """

def lis(a):
    n = len(a)
    lis = [1]*n  
    for i in range (1, n):
        for j in range(0, i):
            if a[i] > a[j] and lis[i] < lis[j] + 1 :
                lis[i] = lis[j] + 1

    m = 0
    for i in range(n):
        m = max(m, lis[i]) 

    return m


def test_lis():
    """ Tests """
    assert(lis([10, 22, 9, 33, 21, 50, 41, 60]) == 5)


if __name__ == '__main__':
    print('LIS of is ', lis([10, 22, 9, 33, 21, 50, 41, 60]))
