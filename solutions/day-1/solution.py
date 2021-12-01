depths_file = open('input.txt', 'r')
# Remove newlines and convert to integer
depths = [(int(line.strip())) for line in depths_file]


def get_num_increased(window_size: int) -> int:
    global depths

    num_increased = 0
    prev = sum(depths[0:window_size])
    for index in range(0, len(depths)):
        # Check if the next window is out of range
        # +1 since non-inclusive end
        if index+window_size+1 > len(depths):
            break

        current = sum(depths[index+1:index+window_size+1])
        if current > prev:
            num_increased += 1

        prev = current

    print(f'Number increased (window_size={window_size}): {num_increased}')
    return num_increased


def main():
    get_num_increased(1)
    get_num_increased(3)


main()
