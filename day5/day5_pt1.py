def read_int():
    return int(raw_input())

def main():
    jmps = list()
    while True:
        try:
            jmps.append(read_int())
        except EOFError:
            break
    i = 0
    steps = 0
    while i >= 0 and i < len(jmps):
        tmp = jmps[i]
        jmps[i] += 1
        i += tmp
        steps += 1
    print steps

if __name__ == "__main__":
    main()