import argparse

def find_common_letters(id1, id2):
    common = ""
    for i in range(len(id1)):
        if id1[i] == id2[i]:
            common += id1[i]
    return (common, len(id1)-len(common))

def main(args):
    ids = []
    with open(args.infile,'r') as file:
        line = file.readline().strip()
        while len(line) > 0:
            ids.append(line)
            line = file.readline().strip()
    diff_size = 2
    common = ""
    for i in range(len(ids)-1):
        if diff_size == 1:
            break
        for j in range(1,len(ids)):
            if diff_size == 1:
                break
            common, diff_size = find_common_letters(ids[i], ids[j])
    print(common)

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('--infile', type=str, default='day2.in', help='Input file.')
    main(parser.parse_args())