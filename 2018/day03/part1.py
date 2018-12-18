import argparse

def create_rows(matrix, n):
    for i in range(n):
        matrix.append([0] * len(matrix[0]))

def create_columns(matrix, n):
    if n > 0:
        for row in matrix:
            row += [0] * n

def adapt(matrix, left_offset, top_offset, width, height):
    expected_column = left_offset + width
    expected_row = top_offset + height
    create_rows(matrix, expected_row + 1 - len(matrix))
    create_columns(matrix, expected_column + 1 - len(matrix[0]))

def parse(line):
    parts = line.split("@")
    #id = int(parts[0].strip("# "))
    parts = parts[1].split(",")
    left_offset = int(parts[0].strip())
    parts = parts[1].split(":")
    top_offset = int(parts[0].strip())
    parts = parts[1].split("x")
    width = int(parts[0].strip())
    height = int(parts[1].strip())
    return left_offset, top_offset, width, height

def main(args):
    fabric = [[0]]
    with open(args.infile,'r') as file:
        line = file.readline().strip()
        while len(line) > 0:
            left_offset, top_offset, width, height = parse(line)
            adapt(fabric, left_offset, top_offset, width, height)
            for i in range(top_offset, top_offset + height):
                for j in range(left_offset, left_offset + width):
                    fabric[i][j] += 1
            line = file.readline().strip()
    count = 0
    #print(fabric)
    for i in range(len(fabric)):
        for j in range(len(fabric[0])):
            if fabric[i][j] > 1:
                count += 1
    print(count)

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('--infile', type=str, default='day3.in', help='Input file.')
    main(parser.parse_args())