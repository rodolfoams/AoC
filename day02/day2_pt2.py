def get_division(arr):
    if len(arr) <= 1:
        return 1

    for i in xrange(len(arr)):
        for j in xrange(i+1, len(arr)):
            if arr[i] % arr[j] == 0:
                return arr[i]/arr[j]

    return max_v - min_v

def read_int_arr():
    return map(int, raw_input().strip().split())

def main():
    checksum = 0
    while True:
        try:
            row = read_int_arr()
            row.sort(reverse=True)
            checksum += get_division(row)
        except EOFError:
            print checksum
            break

if __name__ == "__main__":
    main()