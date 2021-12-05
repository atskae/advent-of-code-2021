import re


class FieldMap:

    def _fill_map(self, skip_diagonals=True):
        for line in self.lines:
            (x1, y1) = line[0]
            (x2, y2) = line[1]
            # print(f"({x1},{y1}) -> ({x2},{y2})")
            if skip_diagonals:
                if not (x1 == x2 or y1 == y2):
                    # print("Skipping")
                    continue

            step = 1
            if x1 == x2:
                # Vertical line
                p1 = y1
                p2 = y2
                if y1 > y2:
                    step = -1
            else:
                # Horizontal line
                p1 = x1
                p2 = x2
                if x1 > x2:
                    step = -1

            # print(f"p1={p1}, p2+step={p2+step}, step={step}")
            for z in range(p1, p2 + step, step):
                if x1 == x2:  # vertical line
                    p = (x1, z)
                else:
                    p = (z, y1)

                if p not in self.map:
                    self.map[p] = 0

                self.map[p] += 1
                if self.map[p] == 2:
                    self.num_overlaps += 1

                # print(f"{p}: {self.map[p]}")

    def __init__(self, lines, skip_diagonals=True):
        self.map = {}
        self.lines = lines
        self.num_overlaps = 0
        self._fill_map(skip_diagonals=skip_diagonals)


def parse_input_file(input_file_name: str) -> list[list[tuple[int, int]]]:
    input_file = open(input_file_name, "r")
    lines = []
    for file_line in input_file:
        file_line = file_line.strip()
        points_str = [point.strip() for point in file_line.split("->")]
        re_pattern = r"(\d+),(\d+)"
        line = []
        for point_str in points_str:
            matches = re.match(re_pattern, point_str)
            point = (int(matches.group(1)), int(matches.group(2)))
            line.append(point)
        lines.append(line)
    return lines


def main():
    input_file_name = "input.txt"
    print(f"Reading in: {input_file_name}")
    lines = parse_input_file(input_file_name)
    field_map_no_diagonals = FieldMap(lines, skip_diagonals=True)
    #for point in sorted(field_map.map.keys()):
    #    print(f"{point}: {field_map.map[point]}")
    print("num_overlaps", field_map_no_diagonals.num_overlaps)


main()
