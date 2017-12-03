def get_diff(arr):
    if len(arr) <= 1:
        return 0

    min_v = arr[0]
    max_v = arr[0]

    for i in xrange(1, len(arr)):
        min_v = arr[i] if min_v > arr[i] else min_v
        max_v = arr[i] if max_v < arr[i] else max_v

    return max_v - min_v

def read_int_arr():
    return map(int, raw_input().strip().split())

def main():
    checksum = 0
    while True:
        try:
            row = read_int_arr()
            checksum += get_diff(row)
        except EOFError:
            print checksum
            break

if __name__ == "__main__":
    main()