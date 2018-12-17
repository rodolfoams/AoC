input_file = "day13.in"

def catch(l, delay):
    l = l.split(":")
    t = int(l[0].strip()) + delay
    r = int(l[1].strip())
    p = (r - 1) * 2
    if t%p == 0:
        return True
    return False

def main():
    f = open(input_file,"r")
    lines = f.readlines()
    f.close()
    caught = True
    delay = 0
    while caught:
        caught = False
        for l in lines:
            if catch(l, delay):
                caught = True
                delay += 1
                break

    print delay

if __name__ == "__main__":
    main()