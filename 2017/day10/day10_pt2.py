SIZE = 256
SUFFIX = [17, 31, 73, 47, 23]
ROUNDS = 64

def jumpify(s):
    jumps = list()
    for c in s:
        jumps.append(ord(c))
    return jumps

def hexify(n):
    res = hex(n)[2:]
    if len(res) == 1: res = "0" + res
    return res

def solve(s):
    circ_list = range(SIZE)
    lengths = jumpify(s) + SUFFIX
    skip_size = 0
    curr_position = 0

    for r in xrange(ROUNDS):
        for l in lengths:
            tmp = list()
            for i in xrange(l):
                tmp.append(circ_list[(curr_position+i)%SIZE])
            tmp.reverse()
            for i in xrange(l):
                circ_list[(curr_position+i)%SIZE] = tmp[i]
            curr_position = (curr_position+l+skip_size)%SIZE
            skip_size += 1
    dense_hash = list()
    for i in xrange(SIZE/16):
        res = 0
        for j in xrange(16):
            res ^= circ_list[16*i+j]
        dense_hash.append(res)
    return ''.join(map(hexify, dense_hash))

def main():
    assert solve("") == "a2582a3a0e66e6e86e3812dcb672a272"
    assert solve("AoC 2017") == "33efeb34ea91902bb2f59c9920caa6cd"
    assert solve("1,2,3") == "3efbe78a8d82f29979031a4aa0b16a9d"
    assert solve("1,2,4") == "63960835bcdc130f0b66d7ff4f6a5a8e"
    print solve("31,2,85,1,80,109,35,63,98,255,0,13,105,254,128,33")

if __name__ == "__main__":
    main()