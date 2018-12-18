import argparse

def get_polarity(unit):
    if unit.isupper():
        return 1
    return 0

def have_same_polarity(unit1, unit2):
    return get_polarity(unit1) == get_polarity(unit2)

def have_same_type(unit1, unit2):
    return unit1.lower() == unit2.lower()

def main(args):
    
    line = ''
    with open(args.infile,'r') as file:
        line = file.readline().strip()
    
    line = list(line)
    reacted = True
    while reacted and len(line) > 1:
        reacted = False
        for i in range(len(line)-2,-1,-1):
            if i == len(line) - 1:
                continue
            unit1 = line[i]
            unit2 = line[i+1]
            if have_same_type(unit1, unit2) and not have_same_polarity(unit1, unit2):
                reacted = True
                line.pop(i)
                line.pop(i)
    # print(len(line))
    print(len(line))


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('--infile', type=str, default='day5.in', help='Input file.')
    main(parser.parse_args())