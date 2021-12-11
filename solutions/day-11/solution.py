class Octopus:

    def __init__(self, init_energy_level):
        self.energy_level = init_energy_level
        self.last_step_flashed = 0

    def __str__(self) -> str:
        return str(self.energy_level)

    def __repr__(self) -> str:
        return self.__str__()

    def increase_energy_level(self) -> int:
        self.energy_level += 1
        return self.energy_level

    def can_flash(self, step) -> bool:
        return self.energy_level > 9 and step > self.last_step_flashed

    def flashed_in_this_step(self, step) -> bool:
        return self.last_step_flashed == step

    def prepare_flash(self, step):
        self.last_step_flashed = step
        self.energy_level = 0


def parse_input_file(input_file_name) -> list[list[int]]:
    print(f"Reading input: {input_file_name}")
    energy_grid = []
    with open(input_file_name, "r") as f:
        for line in f:
            line = line.strip()
            row = [Octopus(int(energy_level)) for energy_level in list(line)]
            energy_grid.append(row)

    return energy_grid


def is_out_of_bounds(energy_grid, row, col) -> bool:
    if row < 0 or col < 0:
        return True
    if row >= len(energy_grid) or col >= len(energy_grid[0]):
        return True

    return False


def _r_try_emit_flash(total_flashes, energy_grid, step, row, col):
    if is_out_of_bounds(energy_grid, row, col):
        return

    if energy_grid[row][col].can_flash(step):
        #print(f"{row},{col} can flash!")
        energy_grid[row][col].prepare_flash(step)
        total_flashes[0] += 1

        adj_positions = [
            (row-1, col),  # north
            (row-1, col+1),  # north-east
            (row, col+1),  # east
            (row+1, col+1),  # south-east
            (row+1, col),  # south
            (row+1, col-1), # south-west
            (row, col-1),  # west
            (row-1, col-1)  # north-west
        ]

        for (adj_row, adj_col) in adj_positions:
            if not is_out_of_bounds(energy_grid, adj_row, adj_col):
                if not energy_grid[adj_row][adj_col].flashed_in_this_step(step):
                    energy_level = energy_grid[adj_row][adj_col].increase_energy_level()
                    #print(f"Received energy at {adj_row},{adj_col}: energy_level={energy_level}")
                    _r_try_emit_flash(total_flashes, energy_grid, step, adj_row, adj_col)


def print_energy_grid(energy_grid):
    for row in energy_grid:
        print(row)


def main():
    input_file_name = "input.txt"
    energy_grid = parse_input_file(input_file_name)
    print_energy_grid(energy_grid)

    max_steps = 100
    num_rows = len(energy_grid)
    num_cols = len(energy_grid[0])
    total_flashes = 0
    first_simultaneous_flash = 0
    total_octopus = num_rows * num_cols
    step = 1
    while first_simultaneous_flash == 0:

        #print(f"=== STEP {step} ===")

        # Increase every energy level
        for row in range(0, num_rows):
            for col in range(0, num_cols):
                energy_grid[row][col].increase_energy_level()

        #print(f"After increasing all in step {step}")
        #print_energy_grid(energy_grid)

        num_flashes = [0]
        for row in range(0, num_rows):
            for col in range(0, num_cols):
                _r_try_emit_flash(num_flashes, energy_grid, step, row, col)

        if num_flashes[0] == total_octopus:
            print(f"* * * FLASH * * *")
            first_simultaneous_flash = step

        if step <= max_steps:
            total_flashes += num_flashes[0]

        print(f"Number of flashes in step {step}: {num_flashes[0]}/{total_octopus}")
        #print_energy_grid(energy_grid)

        step += 1

    print(f"Total flashes in {max_steps} steps: {total_flashes}")
    print(f"First simultaneous flash: step {first_simultaneous_flash}")


main()
