connections = dict()
groups = list()
unvisited_nodes = list()

def parse(l):
    global connections, unvisited_nodes
    l = l.split("<->")
    origin = l[0].strip()
    unvisited_nodes.append(origin)
    dests = l[1].strip().split(",")
    connections[origin] = list()
    for d in dests:
        connections[origin].append(d.strip())

def main():
    global unvisited_nodes, groups
    while True:
        try:
            l = raw_input().strip()
            parse(l)
        except EOFError:
            break
    while len(unvisited_nodes) > 0:
        curr_group = [unvisited_nodes[0]]
        to_visit = list(connections[unvisited_nodes[0]])
        while len(to_visit) > 0:
            tmp = list()
            for n in to_visit:
                if n not in curr_group:
                    curr_group.append(n)
                    for c in connections[n]:
                        if c not in curr_group:
                            tmp.append(c)
            to_visit = list(set(tmp))
        groups.append(list(curr_group))
        for n in curr_group:
            unvisited_nodes.remove(n)
    print len(groups)

if __name__ == "__main__":
    main()