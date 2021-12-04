class Board:
    def __init__(self, board, num_pos):
        self.board = board
        # Mapping: num -> (row, col) position on the board
        self.num_pos = num_pos

    def __str__(self):
        board_str = ""
        for row in self.board:
            board_str += str(row) + '\n'
        return board_str


def parse_input_file(input_file_name: str) -> tuple[list[int], list[Board]]:
    input_file = open(input_file_name, "r")
    print(f'Input file: {input_file_name}')

    nums_drawn = []
    boards = []
    board = []
    row_index = 0
    num_pos = {}
    for line_number, line in enumerate(input_file):
        line = line.strip()  # remove new line
        if line_number == 0:
            nums_drawn = [int(num) for num in line.split(',')]
        else:
            if len(line) == 0:  # starting a new board
                if len(board) > 0:
                    boards.append(Board(board, num_pos))
                board = []
                row_index = 0
                num_pos = {}
            else:
                # Add the board row to the current board
                row = [int(num) for num in line.split()]
                for col_index, num in enumerate(row):
                    if num in num_pos:
                        # Hoping this never happens...
                        print(f"{num} already exists on this board!")
                    num_pos[num] = (row_index, col_index)
                board.append(row)
                row_index += 1

    boards.append(Board(board, num_pos))

    return nums_drawn, boards


def main():
    input_file_name = "example_input.txt"
    nums_drawn, boards = parse_input_file(input_file_name)
    print("nums_drawn", nums_drawn)
    for i, board in enumerate(boards):
        print(f"board {i}")
        print(board)

        for key in board.num_pos.keys():
            print(f"{key}: {board.num_pos[key]}")

main()
