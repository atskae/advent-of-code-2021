from solution import parse_input_file


def main():
    input_file_name = "example_input_small.txt"
    digit_entries = parse_input_file(input_file_name)
    print(digit_entries)

    digit_to_segments = {
        0: frozenset("abcefg"),
        1: frozenset("cf"),
        2: frozenset("acdeg"),
        3: frozenset("acdfg"),
        4: frozenset("bcdf"),
        5: frozenset("abdfg"),
        6: frozenset("abdefg"),
        7: frozenset("acf"),
        8: frozenset("abcdefg"),
        9: frozenset("abcdfg")
    }
    num_segments_to_digit = {
        2: 1,
        3: 7,
        4: 4,
        7: 8
    }

    # number of segments -> segments
    num_segments_to_segments_map = {}
    for digit in digit_to_segments:
        segments = digit_to_segments[digit]
        num_segments = len(segments)
        if num_segments not in num_segments_to_segments_map.keys():
            num_segments_to_segments_map[num_segments] = []
        num_segments_to_segments_map[num_segments].append(segments)

    #for num_segment in num_segments_to_segments_map.keys():
    #    print(f"{num_segment}: {num_segments_to_segments_map[num_segment]}")

    for digit_entry in digit_entries:
        segment_to_segment_map = {}
        for segment in "abcdefg":
            segment_to_segment_map[segment] = set("abcdefg")
        solutions_cache = {}
        non_unique_seen = {
            5: [],
            6: []
        }
        for signal in digit_entry.signals:
            signal = frozenset(signal)
            num_segments = len(signal)
            if num_segments == 7:
                solutions_cache[signal] = num_segments_to_digit[num_segments]
            elif num_segments in non_unique_seen.keys():
                non_unique_seen[num_segments].append(signal)
            else:
                for segment in signal:
                    segment_to_segment_map[segment] &= num_segments_to_segments_map[num_segments][0]
                    if len(segment_to_segment_map[segment]) == 1:
                        s = segment_to_segment_map[segment][0]
                        for seg in segment_to_segment_map.keys():
                            if seg == segment:
                                continue
                            segment_to_segment_map[segment] -= s

                solutions_cache[signal] = num_segments_to_digit[num_segments]

        for segment in segment_to_segment_map.keys():
            print(f"{segment}: {segment_to_segment_map[segment]}")

        for digit in non_unique_seen.keys():
            signals = non_unique_seen[digit]
            common = set()
            total = set
            for signal in signals:
                common &= signal
                total = total.union(signal)
            uncommon = total - common


main()
