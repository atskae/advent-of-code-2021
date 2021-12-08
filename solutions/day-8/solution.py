def main():
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
