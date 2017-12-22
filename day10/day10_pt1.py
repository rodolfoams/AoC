SIZE = 256

def read_int_arr():
    return map(int, raw_input().strip().split(","))

def main():
    circ_list = range(SIZE)
    lengths = read_int_arr()
    skip_size = 0
    curr_position = 0

    for l in lengths:
        tmp = list()
        for i in xrange(l):
            tmp.append(circ_list[(curr_position+i)%SIZE])
        tmp.reverse()
        for i in xrange(l):
            circ_list[(curr_position+i)%SIZE] = tmp[i]
        curr_position = (curr_position+l+skip_size)%SIZE
        skip_size += 1
    print circ_list[0] * circ_list[1]

if __name__ == "__main__":
    main()