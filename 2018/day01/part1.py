import argparse

def main(args):
    frequency = 0
    with open(args.infile,'r') as file:
        line = file.readline().strip()
        while len(line) > 0:
            frequency += int(line)
            line = file.readline().strip()
    print(frequency)

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('--infile', type=str, default='day1.in', help='Input file.')
    main(parser.parse_args())