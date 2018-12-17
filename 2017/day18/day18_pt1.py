from sys import argv

registers = dict()
last_played = 0
idx = 0
instructions = list()

def process_next_instruction():
    global registers, last_played, idx, instructions
    inst = instructions[idx]
    inst_name = inst[0]
    if inst_name == "snd":
        if inst[1].isalpha():
            reg_name = inst[1]
            if reg_name not in registers:
                registers[reg_name] = 0
            last_played = registers[reg_name]
        else:
            sound = int(inst[1])
            last_played = sound
    elif inst_name == "set":
        reg_name = inst[1]
        if inst[2].isalpha():
            reg_src_name = inst[2]
            if reg_src_name not in registers:
                registers[reg_src_name] = 0
            registers[reg_name] = registers[reg_src_name]
        else:
            value = int(inst[2])
            registers[reg_name] = value        
    return 0

def solve(instructions):
    global last_played
    recovered = False
    while not recovered:
        recovered = process_next_instruction()
    return last_played

def main(args):
    global instructions
    with open(args[0],"r") as IF:
        instructions = IF.readlines()
    instructions = map(lambda x: x.strip().split(), instructions)
    ans = solve(instructions)
    if len(args) == 1:
        print ans
    else:
        expected = 0
        with open(args[1],"r") as OF:
            exp_line = OF.readline().strip()
            expected = int(exp_line)
        assert(expected) == ans

if __name__ == "__main__":
    main(argv[1:])