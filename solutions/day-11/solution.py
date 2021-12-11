def parse_input_file(input_file_name) -> list[list[int]]:
    print(f"Reading input: {input_file_name}")
    energy_map = []
    with open(input_file_name, "r") as f:
        for line in f:
            line = line.strip()
            row = [int(light) for light in list(line)]
            energy_map.append(row)

    return energy_map


def main():
    input_file_name = "example_input.txt"
    energy_map = parse_input_file(input_file_name)
    for row in energy_map:
        print(row)


main()
