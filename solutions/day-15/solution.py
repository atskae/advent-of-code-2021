import sys


def parse_input_file(input_file_name) -> list[list[int]]:
    print(f"Reading input: {input_file_name}")
    risk_map = []
    with open(input_file_name, "r") as f:
        for line in f:
            line = line.strip()
            risk_map.append([int(risk) for risk in list(line)])

    if len(risk_map[0]) <= 10:
        for row in risk_map:
            print(row)

    return risk_map


def get_adj(pos):
    row, col = pos
    adj_positions = [
        (row-1, col),  # up
        (row, col+1),  # right
        (row+1, col),  # down
        (row, col-1),  # left
    ]

    return adj_positions


def _r_find_min_risk_path(risk_map, num_rows, num_cols, min_risk, visited, current_risk, pos):
    if pos in visited:
        return

    visited[pos] = True
    row, col = pos
    print(f"Current pos: {pos}, num_rows={num_rows}, num_cols={num_cols}, min_risk={min_risk[0]}")
    if row == num_rows-1 and col == num_cols-1:
        if min_risk[0] is None or current_risk < min_risk[0]:
            min_risk[0] = current_risk
            print(f"Found a min path, total {min_risk[0]}")

        return

    for adj_pos in get_adj(pos):
        adj_row, adj_col = adj_pos
        if (adj_row < 0 or adj_col < 0) or (adj_row >= num_rows or adj_col >= num_cols):
            continue

        new_risk = current_risk + risk_map[adj_row][adj_col]
        if min_risk[0] is None or new_risk < min_risk[0]:
            _r_find_min_risk_path(
                risk_map, num_rows, num_cols, min_risk, dict(visited), new_risk, adj_pos
            )


def main(argv):
    risk_map = parse_input_file(argv[1])

    num_rows = len(risk_map)
    num_cols = len(risk_map[0])
    min_risk = [None]
    start_pos = (0, 0)
    _r_find_min_risk_path(risk_map, num_rows, num_cols, min_risk, {}, 0, start_pos)
    print(f"Min risk: {min_risk[0]}")


if __name__ == "__main__":
    main(sys.argv)
