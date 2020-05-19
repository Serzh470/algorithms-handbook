""" Longest common subsequence (Needleman-Wunsch) """

def lcs(a, b):
    # get matrix with common elements
    M = [[0]*(len(b) + 1) for _ in range(len(a) + 1)]
    for i in range(1, len(a) + 1):
        for j in range(1, len(b) + 1):
            if a[i-1] == b[j-1]:
                M[i][j] =  M[i-1][j-1] + 1
            else:
                M[i][j] = max(M[i-1][j], M[i][j-1])

    # get lcs - restore from matrix
    LCS = []
    i, j = len(a) - 1, len(b) - 1
    while i >= 0 and j >= 0:
        if a[i] == b[j]:
            LCS.append(a[i])
            i, j = i - 1, j - 1
        elif M[i-1][j] > M[i][j-1]:
            i -= 1
        else:
            j -= 1
    LCS.reverse()
    return ''.join(LCS)



def test_lcs():
    """ Tests """
    assert(lcs('abrakadabra', 'kadarbda') == 'kadara')


if __name__ == '__main__':
    print('LCS of "abrakadabra" and "kadarbda" is ', lcs('abrakadabra', 'kadarbda'))
