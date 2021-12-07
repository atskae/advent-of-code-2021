from math import ceil

cost_cache = {}


def parse_input_file(input_file_name) -> list[int]:
    print(f"Reading input: {input_file_name}")
    with open(input_file_name, "r") as f:
        line = f.readline().rstrip()
        return [int(pos) for pos in line.split(",")]


def calculate_cost(num_crabs, current_pos) -> int:
    """Calculate the cost to move all crab to pos"""
    global cost_cache
    if current_pos in cost_cache:
        return cost_cache[current_pos]

    cost = 0
    for pos in num_crabs.keys():
        if pos == current_pos:
            continue
        cost += (abs(current_pos - pos) * num_crabs[pos])
    #print(f"Cost to move to position {current_pos}: {cost}")
    cost_cache[current_pos] = cost
    return cost_cache[current_pos]


def _r_find_min(num_crabs, left_index, right_index) -> tuple[int, int]:
    if left_index == right_index:
        cost = calculate_cost(num_crabs, left_index)
        return left_index, cost

    midpoint = left_index + ceil((right_index - left_index) / 2)
    left_cost = calculate_cost(num_crabs, midpoint-1)
    right_cost = calculate_cost(num_crabs, midpoint)
    if left_cost < right_cost:
        return _r_find_min(num_crabs, left_index, midpoint-1)
    else:
        return _r_find_min(num_crabs, midpoint, right_index)


def main():
    input_file_name = "input.txt"
    horizontal_positions = parse_input_file(input_file_name)
    #print("horizontal_positions", horizontal_positions)

    # Create mapping: position -> # of crabs there
    num_crabs = {}
    max_pos = 0
    for pos in horizontal_positions:
        if pos > max_pos:
            max_pos = pos
        if pos not in num_crabs:
            num_crabs[pos] = 0
        num_crabs[pos] += 1

    print(f"max_pos={max_pos}")
    pos, min_cost = _r_find_min(num_crabs, 0, max_pos)
    print(f"pos={pos}, min_cost={min_cost}")


main()
