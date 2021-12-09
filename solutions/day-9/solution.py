def parse_input_file(input_file_name) -> list[list[int]]:
    print(f"Reading input: {input_file_name}")
    height_map = []
    with open(input_file_name, "r") as f:
        for line in f:
            line = line.strip()
            row = [int(height) for height in list(line)]
            height_map.append(row)

    return height_map


def get_adj_heights(height_map, row, col) -> list[int]:
    """Get the adjacent heights"""
    positions = [
        (row-1, col),  # up
        (row, col+1),  # right
        (row+1, col),  # down
        (row, col-1),  # left
    ]
    adj_heights = []
    for (adj_row, adj_col) in positions:
        if adj_row < 0 or adj_col < 0:
            continue

        try:
            adj_height = height_map[adj_row][adj_col]
            #print(f"Got adj_height={adj_height} at {adj_row},{adj_col}")
            adj_heights.append(adj_height)
        except IndexError:
            pass


    #print(f"adj_heights of row={row},col={col}: {adj_heights}")
    return adj_heights


def main():
    input_file_name = "input.txt"
    height_map = parse_input_file(input_file_name)
    for row in height_map:
        print(row)

    risk_levels = []
    for row in range(0, len(height_map)):
        for col in range(0, len(height_map[row])):
            adj_heights = get_adj_heights(height_map, row, col)
            print(f"row={row}, col={col}")
            print("adj_heights", adj_heights)
            height = height_map[row][col]
            is_lowest_point = True
            for adj_height in adj_heights:
                if adj_height <= height:
                    is_lowest_point = False
                    break

            if is_lowest_point:
                risk_levels.append(height+1)

    print("risk_levels", risk_levels)
    print("sum(risk_levels)", sum(risk_levels))


main()
