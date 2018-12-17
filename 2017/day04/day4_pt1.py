def main():
    ctr = 0
    while True:
        try:
            pp = raw_input().strip().split()
            ctr += 1
            pp.sort()
            for i in xrange(len(pp)-1):
                if pp[i] == pp[i+1]:
                    ctr -= 1
                    break
        except EOFError:
            break
    print ctr
    
if __name__ == "__main__":
    main()