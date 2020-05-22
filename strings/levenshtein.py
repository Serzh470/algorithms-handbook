""" Levenshtein distance """

def levenstein(a, b):
    n = len(a) + 1
    m = len(b) + 1

    matrixD = [[0 for j in range(len(b) + 1)] for i in range(len(a) + 1)]

    deletionCost = 1
    insertionCost = 1

    for i in range(n):
        matrixD[i][0] = i

    for j in range(m):
        matrixD[0][j] = j

    for i in range(1, n):
        for j in range(1, m):
            substitutionCost = 0 if a[i-1] == b[j-1] else 1
            matrixD[i][j] = min (
                matrixD[i-1][j] + deletionCost,
                matrixD[i][j-1]+ insertionCost,
                matrixD[i-1][j-1] + substitutionCost,
            )

    return matrixD[n-1][m-1]




def test_levenstein():
    """ Tests """
    assert(levenstein('abrakadabra', 'kadarbda') == 6)


if __name__ == '__main__':
    print('Levenstein distance of "abrakadabra" and "kadarbda" is ', levenstein('abrakadabra', 'kadarbda'))

