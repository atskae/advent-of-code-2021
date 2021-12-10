from dataclasses import dataclass


@dataclass
class DigitEntry:
    signals: list[str]
    outputs: list[str]


def eliminate_non_matches(segment_to_segment: dict[int, set], segments: set, correct_segments: set) -> bool:
    match_found = False
    for segment in segments:
        current_mapping = segment_to_segment[segment]
        #print(f"current_mapping: {segment}: {current_mapping}")
        to_remove = current_mapping - correct_segments
        #print(f"correct_segments: {correct_segments}")
        #print(f"to_remove: {to_remove}")
        segment_to_segment[segment] -= to_remove
        if len(segment_to_segment[segment]) == 1:
            match_found = True
            segment_to_remove = list(segment_to_segment[segment])[0]
            #print(f"Eliminating {segment_to_remove} from everyone except {segment}")

            # No other segment can match to this one, so remove from others
            for s in segment_to_segment.keys():
                if s == segment:
                    continue
                #print(f"before removal: {s}: {segment_to_segment[s]}, want to remove {segment_to_remove}")
                segment_to_segment[s] -= set(segment_to_remove)
                #print(f"after removal: {s}: {segment_to_segment[s]}")

        #print(f"after: {segment}: {segment_to_segment[segment]}")

    return match_found


def get_digit(segment_to_segment, segments_to_digit, output) -> str:
    translated_segments = ""
    for segment in output:
        translated_segments += segment_to_segment[segment]

    translated_segments = "".join(sorted(translated_segments))
    #print(f"{output} -> {translated_segments}")
    try:
        return str(segments_to_digit[translated_segments])
    except KeyError:
        return None


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
    #print(digit_entries)

    # Part 1
    total_unique = 0
    for digit in digit_entries:
        #print(f"signals: {digit.signals}")
        #print(f"outputs: {digit.outputs}")
        for output in digit.outputs:
            num_segments = len(output)
            if num_segments == 2 or num_segments == 3 or num_segments == 4 or num_segments == 7:
                total_unique += 1
    print(f"Total unique: {total_unique}")

    # Part 2
    correct_num_segments_to_segments = {
        2: [set("cf")],
        3: [set("acf")],
        4: [set("bcdf")],
        5: [set("acdeg"), set("acdfg"), set("abdfg")],
        6: [set("abcefg"), set("abdefg"), set("abcdfg")],
        7: [set("abcdefg")],
    }

    segments_to_digit = {
        "abcefg": 0,
        "cf": 1,
        "acdeg": 2,
        "acdfg": 3,
        "bcdf": 4,
        "abdfg": 5,
        "abdefg": 6,
        "acf": 7,
        "abcdefg": 8,
        "abcdfg": 9
    }

    numbers_to_add = []
    for digit_entry in digit_entries:
        num_segments_to_segments = {}
        for signal in digit_entry.signals:
            signal = sorted(signal)
            num_segments = len(signal)
            if num_segments not in num_segments_to_segments.keys():
                num_segments_to_segments[num_segments] = []

            if set(signal) not in num_segments_to_segments[num_segments]:
                num_segments_to_segments[num_segments].append(set(signal))

        segment_to_segment = {}  # char to char
        for char in set("abcdefg"):
            segment_to_segment[char] = set("abcdefg")

        for num_segments in sorted(num_segments_to_segments.keys()):
            segments = num_segments_to_segments[num_segments]
            #print(f"{num_segments}: {segments}")

            correct_segments = correct_num_segments_to_segments[num_segments]
            common = segments[0]
            correct_common = correct_segments[0]
            for s in segments:
                common &= s
            for s in correct_segments:
                correct_common &= s

            #print(f"common={common}, correct_common={correct_common}")
            eliminate_non_matches(segment_to_segment, common, correct_common)

        for s in sorted(segment_to_segment.keys()):
            #print(f"{s}: {segment_to_segment[s]}")
            assert len(segment_to_segment[s]) == 1
            # Convert to a char mapping
            segment_to_segment[s] = list(segment_to_segment[s])[0]

        final_number = ""
        for output in digit_entry.outputs:
            digit = get_digit(segment_to_segment, segments_to_digit, output)
            assert digit is not None
            final_number += digit
        numbers_to_add.append(int(final_number))

    #print("numbers_to_add", numbers_to_add)
    print(f"sum: {sum(numbers_to_add)}")


main()
