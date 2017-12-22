connections = dict()

def parse(l):
    global connections
    l = l.split("<->")
    origin = l[0].strip()
    dests = l[1].strip().split(",")
    connections[origin] = list()
    for d in dests:
        connections[origin].append(d.strip())

def main():
    while True:
        try:
            l = raw_input().strip()
            parse(l)
        except EOFError:
            break
    group0 = list()
    to_visit = list(connections["0"])
    while len(to_visit) > 0:
        tmp = list()
        for n in to_visit:
            if n not in group0:
                group0.append(n)
                for c in connections[n]:
                    if c not in group0:
                        tmp.append(c)
        to_visit = list(set(tmp))
    print len(group0)

if __name__ == "__main__":
    main()