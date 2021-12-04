class Board:
    def __init__(self, board, num_pos):
        self.board = board
        self.num_rows = len(board)
        self.num_cols = len(board[0])
        # Mapping: num -> (row, col) position on the board
        self.num_pos = num_pos

        self.marked_board = [[False] * self.num_cols for _ in range(self.num_rows)]
        self.last_num_marked = None
        self.won = False

    @staticmethod
    def _get_matrix_str(matrix):
        board_str = ""
        for row in matrix:
            board_str += str(row) + '\n'
        return board_str

    def __str__(self):
        return self._get_matrix_str(self.board)

    def print_marked_board(self):
        print("Marked Board")
        print(self._get_matrix_str(self.marked_board))

    def mark_num(self, num):
        if num not in self.num_pos:
            return
        row, col = self.num_pos[num]
        self.marked_board[row][col] = True
        self.last_num_marked = num

    def is_winner(self) -> bool:
        """This only checks the row and column of the last number marked"""
        if self.last_num_marked not in self.num_pos:
            return False

        row, col = self.num_pos[self.last_num_marked]

        # Check the row of the last number marked
        num_marked_in_row = 0
        for col_index in range(0, self.num_cols):
            if self.marked_board[row][col_index]:
                num_marked_in_row += 1
        if num_marked_in_row == self.num_cols:
            print("Winning row: ", self.board[row])
            self.won = True
            return True

        # Check the column of the last number marked
        num_marked_in_col = 0
        winning_column = []
        for row_index in range(0, self.num_rows):
            if self.marked_board[row_index][col]:
                num_marked_in_col += 1
                winning_column.append(self.board[row_index][col])
        if num_marked_in_col == self.num_rows:
            print("Winning column:")
            for num in winning_column:
                print(num)
            self.won = True
            return True

        return False

    def already_won(self) -> bool:
        return self.won

    def get_sum_unmarked_num(self) -> int:
        unmarked_sum = 0
        for row in range(self.num_rows):
            for col in range(self.num_cols):
                if not self.marked_board[row][col]:
                    unmarked_sum += self.board[row][col]
        return unmarked_sum


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
    input_file_name = "input.txt"
    nums_drawn, boards = parse_input_file(input_file_name)
    for i, board in enumerate(boards):
        print(f"Board # {i}")
        print(board)

    winning_board = None
    losing_board = None
    losing_boards = list(range(len(boards)))
    for num_drawn in nums_drawn:
        print(f"Number drawn: {num_drawn}")
        for i, board in enumerate(boards):
            if board.already_won():
                continue

            board.mark_num(num_drawn)
            if board.is_winner():
                print(f"Board {i} got Bingo!")
                if winning_board is None:
                    print(f"Board {i} is the winner!")
                    winning_board = board

                if len(losing_boards) == 1 and losing_board is None:
                    print(f"Board {i} is the loser...")
                    losing_board = board
                losing_boards.remove(i)

        if losing_board is not None and losing_board.already_won():
            break

    winning_board.print_marked_board()
    sum_unmarked = winning_board.get_sum_unmarked_num()
    puzzle_answer = sum_unmarked * winning_board.last_num_marked
    print(f"Part 1 answer: {sum_unmarked} * {winning_board.last_num_marked} = {puzzle_answer}")

    print("The losing board:")
    print(losing_board)
    losing_board.print_marked_board()
    sum_unmarked = losing_board.get_sum_unmarked_num()
    puzzle_answer = sum_unmarked * losing_board.last_num_marked
    print(f"Part 2 answer: {sum_unmarked} * {losing_board.last_num_marked} = {puzzle_answer}")


main()
