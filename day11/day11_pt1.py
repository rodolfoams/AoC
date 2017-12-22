from day11 import *

def solve(steps):
    steps = steps.split(",")
    curr_pos = [0,0]
    for s in steps:
        if s == "ne":
            curr_pos[0] += 1
            curr_pos[1] += 0.5
        elif s == "n":
            curr_pos[1] += 1
        elif s == "nw":
            curr_pos[0] -= 1
            curr_pos[1] += 0.5
        elif s == "se":
            curr_pos[0] += 1
            curr_pos[1] -= 0.5
        elif s == "s":
            curr_pos[1] -= 1
        elif s == "sw":
            curr_pos[0] -= 1
            curr_pos[1] -= 0.5
    dx = abs(curr_pos[0])
    dy = abs(curr_pos[1]) - dx/2.0
    return dx + max(0, dy)

def main():
    assert solve("ne,ne,ne") == 3
    assert solve("ne,ne,sw,sw") == 0
    assert solve("ne,ne,s,s") == 2
    assert solve("se,sw,se,sw,sw") == 3
    print solve(full)

if __name__ == "__main__":
    main()