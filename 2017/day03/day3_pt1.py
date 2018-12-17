from sys import argv
from math import sqrt

def main(n):
    m_dim = int(sqrt(n)) + 1
    m_dim += m_dim%2 + 2
    m = list()
    for i in xrange(m_dim):
        m.append([0]*m_dim)
    i,j = m_dim/2, m_dim/2 - 1
    pos_one = tuple([i,j])
    i -= 1
    d = "d"
    for k in xrange(1, n+1):
        if d == "d":
            i += 1
            m[i][j] = k
            if m[i][j+1] == 0:
                d = "r"
        elif d == "r":
            j += 1
            m[i][j] = k
            if m[i-1][j] == 0:
                d = "u"
        elif d == "u":
            i -= 1
            m[i][j] = k
            if m[i][j-1] == 0:
                d = "l"
        elif d == "l":
            j -= 1
            m[i][j] = k
            if m[i+1][j] == 0:
                d = "d"

    print abs(i-pos_one[0]) + abs(j-pos_one[1])

if __name__ == "__main__":
    main(int(argv[1]))