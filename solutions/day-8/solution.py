from dataclasses import dataclass


@dataclass
class DigitEntry:
    signals: list[str]
    outputs: list[str]


def parse_input_file(input_file_name) -> list[DigitEntry]:
    print(f"Reading input: {input_file_name}")
    digit_entries = []
    with open(input_file_name, "r") as f:
        for line in f:
            line = line.split("|")
            signal_patterns = line[0].split()
            digit_outputs = line[1].strip().split()
            digit_entries.append(DigitEntry(signals=signal_patterns, outputs=digit_outputs))

    return digit_entries


def main():
    input_file_name = "input.txt"
    digit_entries = parse_input_file(input_file_name)

    total_unique = 0
    for digit in digit_entries:
        print(f"signals: {digit.signals}")
        print(f"outputs: {digit.outputs}")
        for output in digit.outputs:
            num_segments = len(output)
            if num_segments == 2 or num_segments == 3 or num_segments == 4 or num_segments == 7:
                total_unique += 1
    print(f"Total unique: {total_unique}")

    digits = {
        0: ['a', 'b', 'c', 'e', 'f', 'g'],
        1: ['c', 'f'],
        2: ['a', 'c', 'd', 'e', 'g'],
        3: ['a', 'c', 'd', 'f', 'g'],
        4: ['b', 'c', 'd', 'f'],
        5: ['a', 'b', 'd', 'f', 'g'],
        6: ['a', 'b', 'd', 'e', 'f', 'g'],
        7: ['a', 'c', 'f'],
        8: ['a', 'b', 'c', 'd', 'e', 'f', 'g'],
        9: ['a', 'b', 'c', 'd', 'f', 'g']
    }

    segments_map = {}
    for digit in digits.keys():
        segments = digits[digit]
        num_segments = len(segments)
        print(f"{digit}: {num_segments} segments: {segments}")

        if num_segments not in segments_map:
            segments_map[num_segments] = []

        segments_map[num_segments].append(digit)

    for num_segments in sorted(segments_map.keys()):
        print(f"Digits with {num_segments} segments: {segments_map[num_segments]}")


main()
