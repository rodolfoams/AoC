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

def binify(n):
    res = bin(n)[2:]
    while len(res) < 4:
        res = "0" + res
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
    hex_hash = ''.join(map(hexify, dense_hash))
    res = ""
    for c in hex_hash:
        res += binify(int(c,16))
    return res

def main():
    ctr = 0
    for i in xrange(128):
        ctr += solve("vbqugkhl-" + str(i)).count("1")
    print ctr

if __name__ == "__main__":
    main()