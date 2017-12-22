def parse(l):
    l = l.split(":")
    t = int(l[0].strip())
    r = int(l[1].strip())
    p = (r - 1) * 2
    if t%p == 0:
        return t*r
    return 0

def main():
    severity = 0
    while True:
        try:
            l = raw_input().strip()
            severity += parse(l)

        except EOFError:
            break
    print severity

if __name__ == "__main__":
    main()