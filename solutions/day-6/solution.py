def parse_input_file(input_file_name: str) -> list[int]:
    """Returns a list: index -> number of fish with that timer value"""
    print(f"Reading: {input_file_name}")
    lantern_fish = [0] * 9  # "Day 8" = index 9 ^^'
    for line in open(input_file_name, "r"):
        line = line.strip()
        for timer in line.split(","):
            lantern_fish[int(timer)] += 1
    return lantern_fish


def get_total_fish(lantern_fish: list[int]) -> int:
    total_fish = 0
    for num_fish in lantern_fish:
        total_fish += num_fish
    return total_fish


def main():
    input_file_name = "input.txt"
    lantern_fish = parse_input_file(input_file_name)

    max_days = 256
    for day in range(1, max_days+1):
        new_fish = lantern_fish[0]
        for timer in range(1, 9):
            if lantern_fish[timer] == 0:
                continue

            lantern_fish[timer-1] += lantern_fish[timer]
            lantern_fish[timer] = 0

        lantern_fish[0] -= new_fish
        lantern_fish[6] += new_fish
        lantern_fish[8] += new_fish

        if day == 80:
            print(f"Total fish after {day} days: {get_total_fish(lantern_fish)}")

    total_fish = get_total_fish(lantern_fish)
    print(f"Total fish after {max_days} days: {total_fish}")


main()
