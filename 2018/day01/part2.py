import argparse

def main(args):
    deltas = list()
    known_frequencies = {}
    with open(args.infile,'r') as file:
        line = file.readline().strip()
        while len(line) > 0:
            deltas.append(int(line))
            line = file.readline().strip()
    frequency = 0
    i = 0
    while frequency not in known_frequencies:
        known_frequencies[frequency] = 1
        frequency += deltas[i%len(deltas)]
        i += 1
    print(frequency)

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('--infile', type=str, default='day1.in', help='Input file.')
    main(parser.parse_args())