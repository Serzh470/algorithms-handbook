""" 
Substring search. Knuth–Morris–Pratt 
useful link https://www.youtube.com/watch?v=7g-WEBj3igk
"""

def kmp(text, substring):
    # build prefix function
    p = [0] * len(substring)
    i = 1
    j = 0
    while i < len(substring):
        if substring[i] == substring[j]:
            p[i] = j + 1
            i += 1
            j += 1
        elif substring[i] != substring[j]:
            if j == 0:
                i += 1
            else: 
                j = p[j-1]

    # # search substring
    k = 0
    l = 0
    while k < len(text):
        if text[k] == substring[l]:
            l += 1
            if l == len(substring):
                # substring has been found
                return k - l + 1
            k += 1

        elif text[k] != substring[l]:
            if l == 0:
                k += 1
                if k == len(text):
                    return None
            else:
                l = p[l-1]


def test_kmp():
    """ Tests """
    assert(kmp('abcabeabcabcabd', 'abcabd') == 9)


if __name__ == '__main__':
    print('Start index of substring "abcabd" in text "abcabeabcabcabd" is ', 
        kmp('abcabeabcabcabd', 'abcabd'))
