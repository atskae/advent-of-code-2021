import sys


def parse_input_file(input_file_name):
    print(f"Reading input: {input_file_name}")
    with open(input_file_name, "r") as f:
        for line in f:
            line = line.strip()
            pass


def main(argv):
    parse_input_file(argv[1])


if __name__ == "__main__":
    main(sys.argv)
