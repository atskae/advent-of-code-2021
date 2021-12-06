def parse_input_file(input_file_name: str) -> list[int]:
    print(f"Reading: {input_file_name}")
    lantern_fish = []
    for line in open(input_file_name, "r"):
        line = line.strip()
        for fish_id, timer in enumerate(line.split(",")):
            lantern_fish.append(int(timer))
    return lantern_fish


def main():
    input_file_name = "input.txt"
    lantern_fish = parse_input_file(input_file_name)
    #for fish_id, timer in enumerate(lantern_fish):
    #    print(f"<#{fish_id}>< : {timer}")

    max_days = 80
    for day in range(1, max_days+1):
        new_fish = []
        for fish_id, timer in enumerate(lantern_fish):
            if timer == 0:
                new_fish.append(8)
                lantern_fish[fish_id] = 6
            else:
                lantern_fish[fish_id] -= 1
        lantern_fish += new_fish

        if day == 18:
            print(f"Total fish after {day} days: {len(lantern_fish)}")

    print(f"Total fish after {max_days} days: {len(lantern_fish)}")


main()
