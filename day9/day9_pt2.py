def solve(inp):
    total_score = 0
    cleaned_chars = 0
    curr_value = 0
    garbage = False
    ignored = False
    for i in xrange(len(inp)):
        if ignored:
            ignored = False
            continue
        if inp[i] == "!":
            ignored = True
            continue
        if garbage and inp[i] == ">":
            garbage = False
            continue
        if garbage:
            cleaned_chars += 1
        if not garbage:
            if inp[i] == "<":
                garbage = True
                continue
            if inp[i] == "{":
                curr_value += 1
                continue
            if inp[i] == "}":
                total_score += curr_value
                curr_value -= 1

    print cleaned_chars

def main():
    while True:
        try:
            inp = raw_input().strip()
            solve(inp)

        except EOFError:
            break

if __name__ == "__main__":
    main()