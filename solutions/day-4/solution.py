def parse_input_file(input_file_name: str) -> tuple[list[int], list[list[int]]]:
    input_file = open(input_file_name, "r")
    print(f'Input file: {input_file}')

    nums_drawn = []
    boards = []
    board = []  # current board being parsed
    for line_number, line in enumerate(input_file):
        line = line.strip()  # remove new line
        print(f"{line_number}: {line}")
        if line_number == 0:
            nums_drawn = [int(num) for num in line.split(',')]
        else:
            if len(line) == 0:
                boards.append([])
            else:
                # Add the board row to the current board
                boards[-1].append([int(num) for num in line.split()])

    return nums_drawn, boards


def main():
    input_file_name = "example_input.txt"
    nums_drawn, boards = parse_input_file(input_file_name)
    print("nums_drawn", nums_drawn)
    for i, board in enumerate(boards):
        print(f"board {i}", board)


main()
