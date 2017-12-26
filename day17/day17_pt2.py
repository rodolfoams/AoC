def main():
    jump = 371
    size_before = 0
    total_size = 1
    curr_pos = 0
    post_zero = -1
    for i in xrange(50000000):
        curr_pos = (curr_pos + jump + 1) % total_size
        if curr_pos < size_before:
            size_before += 1
        elif curr_pos == size_before:
            post_zero = i+1
        total_size += 1

    print post_zero

if __name__ == "__main__":
    main()