input_file = open('input.txt', 'r')
steps = [(line.strip()) for line in input_file]
steps = [(step.split(' ')[0], int(step.split(' ')[1])) for step in steps]


def get_horizontal_pos_and_depth() -> tuple[int, int]:
    global steps
    final_horizontal_pos = 0
    final_depth = 0

    for index, (direction, amount) in enumerate(steps):
        if index < 10:
            print(f"{index}: final_horizontal_pos={final_horizontal_pos}, final_depth={final_depth}")
            print(f"{index}: direction={direction}, amount={amount}")

        if direction == "forward":
            final_horizontal_pos += amount
        elif direction == "down":
            final_depth += amount
        elif direction == "up":
            final_depth -= amount
        else:
            print(f"Unknown direction: {direction}. Skipping...")

    return final_horizontal_pos, final_depth


def main():
    horizontal_pos, depth = get_horizontal_pos_and_depth()
    print(f'horizontal_pos={horizontal_pos}, depth={depth}')
    print(f'horizontal_pos * depth = {horizontal_pos * depth}')


main()
