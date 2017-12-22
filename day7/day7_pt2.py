weight = dict()
sons = dict()
father = dict()
subtree_weight = dict()
nodes = list()

def parse(line):
    global weight, sons, father, nodes
    line_father = None
    line_sons = list()
    if "->" in line:
        line_sons = line.split("->")[1].split(",")
        for i in xrange(len(line_sons)):
            line_sons[i] = line_sons[i].strip()
        line = line.split("->")[0].strip()
    line = line.split(" ")
    for i in xrange(len(line)):
        line[i] = line[i].strip()
    line_father = line[0]
    nodes.append(line_father)
    weight[line_father] = int(line[1][1:-1])
    if len(line_sons) > 0:
        sons[line_father] = list()
        for s in line_sons:
            sons[line_father].append(s)
            father[s] = line_father

def populate_subtree_weight(root):
    global weight, sons, subtree_weight
    curr_weight = weight[root]
    if root in sons:
        for s in sons[root]:
            populate_subtree_weight(s)
            curr_weight += subtree_weight[s]
    subtree_weight[root] = curr_weight

def solve_unbalanced(node, diff):
    global sons, subtree_weight, weight
    if node not in sons:
        return weight[node] + diff

    node_sons_weights = list()
    for s in sons[node]:
        node_sons_weights.append(subtree_weight[s])
    if len(set(node_sons_weights)) == 1:
        return weight[node] + diff
    wrong_weight = None
    if diff > 0:
        wrong_weight = min(node_sons_weights)
    else:
        wrong_weight = max(node_sons_weights)
    return solve_unbalanced(sons[node][node_sons_weights.index(wrong_weight)],diff)

def solve():
    global weight, sons, father, nodes, subtree_weight
    root = None
    for n in nodes:
        if n not in father:
            root = n
            break
    populate_subtree_weight(root)
    diff = None
    wrong_weight = None
    wrong_node = None
    root_sons_weights = list()
    for s in sons[root]:
        root_sons_weights.append(subtree_weight[s])
    for i in xrange(len(root_sons_weights)):
        if root_sons_weights.count(root_sons_weights[i]) == 1:
            wrong_weight = root_sons_weights[i]
            wrong_node = sons[root][i]
    if wrong_weight < max(root_sons_weights):
        diff = max(root_sons_weights) - wrong_weight
    else:
        diff = min(root_sons_weights) - wrong_weight
    new_weight = solve_unbalanced(wrong_node, diff)
    print new_weight

def main():
    while True:
        try:
            line = raw_input().strip()
            parse(line)
        
        except EOFError:
            break
    solve()

if __name__ == "__main__":
    main()