import argparse

def main(args):
    has_two = 0
    has_three = 0
    with open(args.infile,'r') as file:
        line = file.readline().strip()
        while len(line) > 0:
            counter = {}
            for letter in line:
                if letter not in counter:
                    counter[letter] = 0
                counter[letter] += 1
            found_two = False
            found_three = False
            for letter in line:
                if found_three and found_two:
                    break
                if counter[letter] == 2:
                    found_two = True
                if counter[letter] == 3:
                    found_three = True
            has_two += int(found_two)
            has_three += int(found_three)
            line = file.readline().strip()
    print(has_two * has_three)

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('--infile', type=str, default='day2.in', help='Input file.')
    main(parser.parse_args())