import sys


def parse_input_file(input_file_name):
    print(f"Reading input: {input_file_name}")

    template = None
    rules = {}
    with open(input_file_name, "r") as f:
        for line in f:
            line = line.strip()
            if "->" in line:
                rule = line.split(" -> ")
                rules[rule[0]] = rule[1]
            else:
                if len(line) > 0:
                    template = line

    print(f"template: {template}")
    for pair in rules.keys():
        print(f"{pair} -> {rules[pair]}")

    return template, rules


def main(argv):
    template, rules = parse_input_file(argv[1])

    max_steps = 10
    polymer = template[:]
    new_polymer = polymer[:]
    for step in range(1, max_steps+1):

        num_inserted = 0
        for left_index in range(0, len(polymer)-1):
            pair = polymer[left_index:left_index+2]  # exclusive
            if pair in rules:
                element = rules[pair]
                insert_index = left_index + 1 + num_inserted
                new_polymer = new_polymer[:insert_index] + element + new_polymer[insert_index:]
                num_inserted += 1

        polymer = new_polymer[:]

    counts = {}
    for element in polymer:
        if element not in counts:
            counts[element] = 0
        counts[element] += 1

    counts = sorted(counts.items(), key=lambda e: e[1])
    least_common = counts[0]
    most_common = counts[-1]
    print("Element counts", counts)
    print(f"Least common: {least_common}")
    print(f"Most common: {most_common}")

    difference = most_common[1] - least_common[1]
    print(f"{most_common[1]} - {least_common[1]} = {difference}")


if __name__ == "__main__":
    main(sys.argv)
