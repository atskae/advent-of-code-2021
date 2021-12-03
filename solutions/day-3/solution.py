from copy import deepcopy


def get_rates_for_power_consumption(binary_nums: list[str]) -> tuple[int, int]:
    # Create a mapping: column # -> # of zeros
    # # of ones = # rows - # zeros
    num_columns = len(binary_nums[0])
    num_rows = len(binary_nums)
    num_zeros_by_column = [0] * num_columns

    for binary_num in binary_nums:
        for column, bit in enumerate(binary_num):
            if bit == "0":
                num_zeros_by_column[column] += 1

    print('num_zeros_by_column', num_zeros_by_column)
    gamma_rate_str = "".join(["0" if num_zeros > num_rows/2 else "1" for num_zeros in num_zeros_by_column])
    # I can't just perform ~gamma_rate here... :(
    epsilon_rate_str = "".join(["0" if bit == "1" else "1" for bit in gamma_rate_str])

    gamma_rate = int(gamma_rate_str, 2)
    epsilon_rate = int(epsilon_rate_str, 2)
    return gamma_rate, epsilon_rate


def get_rate_for_life_support(binary_nums: list[str], get_oxygen_generator=True) -> int:
    num_columns = len(binary_nums[0])

    selected_binary_nums = deepcopy(binary_nums)  # copy since will modify
    rating = 0
    for column in range(0, num_columns):
        matches_with_zero = []
        matches_with_one = []
        for binary_num in selected_binary_nums:
            bit = binary_num[column]
            if bit == "0":
                matches_with_zero.append(binary_num)
            else:
                matches_with_one.append(binary_num)

        if get_oxygen_generator:
            # Compute the oxygen generator rating
            if len(matches_with_zero) > len(matches_with_one):
                selected_binary_nums = matches_with_zero
            else:
                selected_binary_nums = matches_with_one
        else:
            # Compute the CO2 scrubber rating
            if len(matches_with_one) < len(matches_with_zero):
                selected_binary_nums = matches_with_one
            else:
                selected_binary_nums = matches_with_zero

        if len(selected_binary_nums) == 1:
            rating = selected_binary_nums[0]
            break

    return int(rating, 2)


def main():
    input_file = open("input.txt", "r")
    binary_nums = [(line.strip()) for line in input_file]

    gamma_rate, epsilon_rate = get_rates_for_power_consumption(binary_nums)
    formatter = f"0{len(binary_nums[0])}b"
    print(f"gamma_rate={gamma_rate}, {format(gamma_rate, formatter)}")
    print(f"epsilon_rate={epsilon_rate}, {format(epsilon_rate, formatter)}")
    power_consumption = gamma_rate * epsilon_rate
    print(f"power_consumption: {power_consumption}")

    oxygen_generator_rating = get_rate_for_life_support(binary_nums, get_oxygen_generator=True)
    co2_scrubber_rating = get_rate_for_life_support(binary_nums, get_oxygen_generator=False)
    print(f"oxygen_generator_rating: {oxygen_generator_rating}")
    print(f"co2_scrubber_rating: {co2_scrubber_rating}")
    life_support_rating = oxygen_generator_rating * co2_scrubber_rating
    print(f"life_support_rating: {life_support_rating}")


main()
