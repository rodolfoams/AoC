def spin(programs, reps):
    for i in xrange(reps):
        programs.insert(0, programs.pop())

def exchange(programs, posA, posB):
    tmp = programs[posA]
    programs[posA] = programs[posB]
    programs[posB] = tmp

def partner(programs, A, B):
    posA = programs.index(A)
    posB = programs.index(B)
    exchange(programs, posA, posB)

def perform(programs, move):
    if move.startswith("s"):
        reps = int(move[1:])
        spin(programs, reps)

    elif move.startswith("x"):
        pos = map(int, move[1:].split("/"))
        exchange(programs, pos[0], pos[1])

    else:
        part = move[1:].split("/")
        partner(programs, part[0], part[1])

def dance(programs, moves):
    for m in moves:
        perform(programs, m)

def main():
    programs_sample = list("abcde")
    programs_full = list("abcdefghijklmnop")

    moves_sample = "s1,x3/4,pe/b".split(",")
    moves_full = raw_input().strip().split(",")

    dance(programs_sample, moves_sample)
    assert("".join(programs_sample) == "baedc")
    
    recorded_positions = list()

    ctr = 0
    for i in xrange(1000000000):
        dance(programs_full, moves_full)
        curr_arrangement = "".join(programs_full)
        if  curr_arrangement in recorded_positions:
            break
        recorded_positions.append(curr_arrangement)
    print recorded_positions[1000000000%len(recorded_positions)-1]

if __name__ == "__main__":
    main()