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

def knot_hash(s):
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

def join_groups(grid, v1, v2, row):
    for i in xrange(row+1):
        grid[i] = map(lambda x: v1 if x == v2 else x, grid[i])

def gen_groups(grid):
    curr_group = 1
    for i in xrange(len(grid)):
        for j in xrange(len(grid[i])):
            if grid[i][j] == ".": continue
            new_group = True
            grid[i][j] = curr_group
            if i > 0:
                if grid[i-1][j] != ".":
                    new_group = False
                    grid[i][j] = grid[i-1][j]
            if j > 0:
                if grid[i][j-1] != ".":
                    grid[i][j] = grid[i][j-1]
                    if not new_group:
                        tmp_min = min(grid[i-1][j], grid[i][j-1])
                        tmp_max = max(grid[i-1][j], grid[i][j-1])
                        join_groups(grid, tmp_min, tmp_max, i)
                    else:
                        new_group = False
            if new_group:
                curr_group += 1

    return grid

def solve(key):
    grid = list()
    for i in xrange(128):
        grid.append(map(lambda x: "." if x == "0" else 1,list(knot_hash(key + "-" + str(i)))))
    gen_groups(grid)
    groups = list()
    for l in grid:
        groups = list(set(groups + list(set(l))))
    return len(groups)-1


def main():
    assert solve("flqrgnkx") == 1242
    print solve("vbqugkhl")

if __name__ == "__main__":
    main()