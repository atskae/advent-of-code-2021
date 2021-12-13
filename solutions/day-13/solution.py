from collections import namedtuple
from enum import Enum
import sys


Dot = namedtuple("Dot", "x,y")

class FoldDirection(Enum):
    x = 'x'
    y = 'y'


Fold = namedtuple("Fold", "dir,value")


def parse_input_file(input_file_name) -> tuple[set[Dot], list[Fold]]:
    print(f"Reading input: {input_file_name}")

    dots = set()
    folds = []
    with open(input_file_name, "r") as f:
        for line in f:
            line = line.strip()
            if "fold along" in line:
                line = line.split(' ')[2]
                line = line.split('=')
                direction = line[0]
                value = int(line[1])
                folds.append(Fold(FoldDirection[direction], value))
            else:  # dot coordinate
                line = line.split(',')
                if len(line) != 2:
                    continue
                x = int(line[0])
                y = int(line[1])
                dot = Dot(x, y)
                dots.add(dot)

    return dots, folds


def main(argv):
    dots, folds = parse_input_file(argv[1])
    print(f"{len(dots)} dots")

    for i, fold in enumerate(folds):
        to_add = set()
        to_remove = set()

        if fold.dir == FoldDirection.x:  # vertical line
            for dot in dots:
                if dot.x > fold.value:
                    diff = dot.x - fold.value
                    to_add.add(Dot(fold.value - diff, dot.y))
                    to_remove.add(dot)
        else:  # horizontal line
            for dot in dots:
                if dot.y > fold.value:
                    diff = dot.y - fold.value
                    to_add.add(Dot(dot.x, fold.value - diff))
                    to_remove.add(dot)

        dots.difference_update(to_remove)
        dots.update(to_add)
        if i+1 == 1:
            print(f"{len(dots)} after fold # {i+1}")

    print(f"{len(dots)} dots after {len(folds)} folds")

    # Print by row
    row_major = {}
    for dot in sorted(dots, key=lambda d: d.y):
        row = dot.y
        if row not in row_major:
            row_major[row] = []
        row_major[row].append(dot)

    for row in row_major.keys():
        prev_dot = Dot(0, row)
        for dot in sorted(row_major[row], key=lambda d: d.x):
            num_empty = dot.x - prev_dot.x - 1
            for _ in range(num_empty):
                print(".", end='')
            print("#", end='')
            prev_dot = dot

        # Print new line
        print("")


if __name__ == "__main__":
    main(sys.argv)

