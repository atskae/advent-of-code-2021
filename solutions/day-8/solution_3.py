from solution import parse_input_file


def eliminate_non_matches(segment_to_segment: dict[int, set], segments: set, correct_segments: set) -> bool:
    match_found = False
    for segment in segments:
        current_mapping = segment_to_segment[segment]
        print(f"current_mapping: {segment}: {current_mapping}")
        to_remove = current_mapping - correct_segments
        print(f"correct_segments: {correct_segments}")
        print(f"to_remove: {to_remove}")
        segment_to_segment[segment] -= to_remove
        if len(segment_to_segment[segment]) == 1:
            match_found = True
            segment_to_remove = list(segment_to_segment[segment])[0]
            print(f"Eliminating {segment_to_remove} from everyone except {segment}")

            # No other segment can match to this one, so remove from others
            for s in segment_to_segment.keys():
                if s == segment:
                    continue
                print(f"before removal: {s}: {segment_to_segment[s]}, want to remove {segment_to_remove}")
                segment_to_segment[s] -= set(segment_to_remove)
                print(f"after removal: {s}: {segment_to_segment[s]}")

        print(f"after: {segment}: {segment_to_segment[segment]}")

    return match_found


def main():
    input_file_name = "example_input_small.txt"
    digit_entries = parse_input_file(input_file_name)
    print(digit_entries)

    num_segments_to_segments = {}
    for digit_entry in digit_entries:
        for signal in digit_entry.signals:
            signal = sorted(signal)
            num_segments = len(signal)
            if num_segments not in num_segments_to_segments.keys():
                num_segments_to_segments[num_segments] = []

            if set(signal) not in num_segments_to_segments[num_segments]:
                num_segments_to_segments[num_segments].append(set(signal))

    correct_num_segments_to_segments = {
        2: [set("cf")],
        3: [set("acf")],
        4: [set("bcdf")],
        5: [set("acdeg"), set("acdfg"), set("abdfg")],
        6: [set("abcefg"), set("abdefg"), set("abcdfg")],
        7: [set("abcdefg")],
    }

    segment_to_segment = {}  # char to char
    for char in set("abcdefg"):
        segment_to_segment[char] = set("abcdefg")

    for num_segments in sorted(num_segments_to_segments.keys()):
        segments = num_segments_to_segments[num_segments]
        print(f"{num_segments}: {segments}")

        correct_segments = correct_num_segments_to_segments[num_segments]

        common = segments[0]
        correct_common = correct_segments[0]
        for s in segments:
            common &= s
        for s in correct_segments:
            correct_common &= s

        print(f"common={common}, correct_common={correct_common}")
        eliminate_non_matches(segment_to_segment, common, correct_common)

    print("---")
    for s in sorted(segment_to_segment.keys()):
        print(f"{s}: {segment_to_segment[s]}")
        assert len(segment_to_segment[s]) == 1



main()
