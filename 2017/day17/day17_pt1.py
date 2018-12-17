def main():
    jump = 3
    buffer = [0]
    curr_pos = 0
    for i in xrange(1, 2018):
        curr_pos = (curr_pos + 372) % len(buffer)
        buffer.insert(curr_pos, i)
    print buffer[(curr_pos + 1) % len(buffer)]

if __name__ == "__main__":
    main()