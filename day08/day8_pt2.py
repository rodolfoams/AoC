operators = ["==", ">=", "<=", "!=", ">", "<", "inc", "dec"]
global_max = 0

registers = dict()

def execute(stmt):
    global registers, operators, global_max
    op = None
    for o in operators:
        if o in stmt:
            op = o
            stmt = stmt.split(o)
            break
    reg = stmt[0].strip()
    if reg not in registers:
        registers[reg] = 0
    v = int(stmt[1].strip())
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
    if op == "inc":
        registers[reg] += v
    elif op == "dec":
        registers[reg] -= v
    global_max = max(global_max, registers[reg])

def main():
    global registers, global_max
    while True:
        try:
            line = raw_input().strip().split("if")
            stmt0 = line[0].strip()
            stmt1 = line[1].strip()
            if execute(stmt1):
                execute(stmt0)            

        except EOFError:
            break
    print global_max

if __name__ == "__main__":
    main()