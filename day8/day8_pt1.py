cond_operators = ["==", ">=", "<=", "!=", ">", "<"]
inst_operators = ["inc", "dec"]

registers = dict()

def check(cond):
    global registers, cond_operators
    op = None
    for o in cond_operators:
        if o in cond:
            op = o
            cond = cond.split(o)
            break
    reg = cond[0].strip()
    if reg not in registers:
        registers[reg] = 0
    v = int(cond[1].strip())
    if op == "==":
        return registers[reg] == v
    if op == ">=":
        return registers[reg] >= v
    if op == "<=":
        return registers[reg] <= v
    if op == "!=":
        return registers[reg] != v
    if op == ">":
        return registers[reg] > v
    if op == "<":
        return registers[reg] < v

def execute(inst):
    global registers, inst_operators
    op = None
    for o in inst_operators:
        if o in inst:
            op = o
            inst = inst.split(o)
            break
    reg = inst[0].strip()
    if reg not in registers:
        registers[reg] = 0
    v = int(inst[1].strip())
    if op == "inc":
        registers[reg] += v
    elif op == "dec":
        registers[reg] -= v

def main():
    global registers
    while True:
        try:
            line = raw_input().strip().split("if")
            inst = line[0].strip()
            cond = line[1].strip()
            if check(cond):
                execute(inst)            

        except EOFError:
            break
    print max(registers.values())

if __name__ == "__main__":
    main()