import re


class FieldMap:

    def __init__(self, input_file_name):
        self.map = {}
        self.lines = []
        self.num_overlaps = 0

        input_file = open(input_file_name, "r")
        for file_line in input_file:
            file_line = file_line.strip()
            points_str = [point.strip() for point in file_line.split("->")]
            re_pattern = r"(\d+),(\d+)"
            line = []
            for point_str in points_str:
                matches = re.match(re_pattern, point_str)
                point = (int(matches.group(1)), int(matches.group(2)))
                line.append(point)
            self.lines.append(line)

        # Fill in the map
        for line in self.lines:
            (x1, y1) = line[0]
            (x2, y2) = line[1]
            #print(f"({x1},{y1}) -> ({x2},{y2})")
            if not (x1 == x2 or y1 == y2):
                #print("Skipping")
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

            #print(f"p1={p1}, p2+step={p2+step}, step={step}")
            for z in range(p1, p2+step, step):
                if x1 == x2:  # vertical line
                    p = (x1, z)
                else:
                    p = (z, y1)

                if p not in self.map:
                    self.map[p] = 0

                self.map[p] += 1
                if self.map[p] == 2:
                    self.num_overlaps += 1

                #print(f"{p}: {self.map[p]}")


def main():
    input_file_name = "input.txt"
    print(f"Reading in: {input_file_name}")
    field_map = FieldMap(input_file_name)
    #for point in sorted(field_map.map.keys()):
    #    print(f"{point}: {field_map.map[point]}")
    print("num_overlaps", field_map.num_overlaps)


main()
