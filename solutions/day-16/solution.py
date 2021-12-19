from collections import namedtuple
from dataclasses import dataclass
from enum import Enum
import sys

IndexRange = namedtuple("IndexRange", "start,end")


class PacketType(Enum):
    Literal = "Literal"
    Operator = "Operator"


@dataclass
class Packet:
    version: int
    type_id: PacketType
    literal_value: int

    def __str__(self):
        s = "---------- Packet ----------\n"
        s += f"Version {self.version}\n"
        s += f"Type ID: {self.type_id}\n"
        s += f"Literal value: {self.literal_value}\n"
        s += "----------------------------"
        return s


def parse_input_file(input_file_name) -> list[str]:
    print(f"Reading input: {input_file_name}")

    bit_strings = []
    with open(input_file_name, "r") as f:
        for line in f:
            line = line.strip()
            print(line)
            num_bits = len(line) * 4
            bit_string = bin(int(line, 16))[2:]  # remove 0b prefix
            bit_string = bit_string.zfill(num_bits)
            bit_strings.append(bit_string)

    return bit_strings


def get_literal_value_from_sub_packet(bit_string, start_index) -> tuple[int, int]:

    # Combine each group to form the literal value
    literal_value = ""
    group_index = start_index
    while group_index < len(bit_string):
        prefix_bit = int(bit_string[group_index], 2)

        # Read the next 4 bits after the prefix bit
        literal_value += bit_string[group_index + 1:group_index + 5]
        group_index += 5

        if prefix_bit == 0:  # last group
            break

    return int(literal_value, 2), group_index


def _r_decode_sub_packets(bit_string, packets, start_index) -> int:

    # Header is 6-bits
    if start_index + 6 >= len(bit_string):
        return start_index

    # Define index ranges
    version_range = IndexRange(start_index, start_index+3)
    type_id_range = IndexRange(version_range.end, version_range.end+3)

    version = int(bit_string[version_range.start:version_range.end], 2)
    if int(bit_string[type_id_range.start:type_id_range.end], 2) == 4:
        type_id = PacketType.Literal
        literal_value, group_index = get_literal_value_from_sub_packet(bit_string, type_id_range.end)
        packet = Packet(version=version, type_id=type_id, literal_value=literal_value)
        packets.append(packet)
        return group_index
    else:
        type_id = PacketType.Operator
        length_type_id_range = IndexRange(type_id_range.end, type_id_range.end + 1)
        length_type_id = int(bit_string[length_type_id_range.start:length_type_id_range.end], 2)
        packet = Packet(version=version, type_id=type_id, literal_value=None)
        packets.append(packet)

        if length_type_id == 0:
            # Read the next 15 bits
            num_bits_range = IndexRange(length_type_id_range.end, length_type_id_range.end + 15)
            total_length_in_bits = int(bit_string[num_bits_range.start:num_bits_range.end], 2)
            print(f"Total length in bits: {total_length_in_bits}")

            sub_packet_start_index = num_bits_range.end
            while sub_packet_start_index < num_bits_range.end + total_length_in_bits:
                sub_packet_start_index = _r_decode_sub_packets(bit_string, packets, sub_packet_start_index)

            return sub_packet_start_index

        elif length_type_id == 1:
            # Read the next 11 bits
            num_sub_packets_range = IndexRange(length_type_id_range.end, length_type_id_range.end + 11)
            num_sub_packets = int(bit_string[num_sub_packets_range.start:num_sub_packets_range.end], 2)
            max_num_sub_packets = len(packets) + num_sub_packets
            print(f"Max number of sub packets: {max_num_sub_packets}")

            sub_packet_start_index = num_sub_packets_range.end
            while len(packets) < max_num_sub_packets:
                sub_packet_start_index = _r_decode_sub_packets(bit_string, packets, sub_packet_start_index)

            return sub_packet_start_index

        else:
            print("Corrupt packet!")
            return -1


def decode_packet(bit_string, packets):
    start_index = 0
    while start_index+6 < len(bit_string):
        start_index = _r_decode_sub_packets(bit_string, packets, start_index)


def main(argv):
    bit_strings = parse_input_file(argv[1])

    packets = []
    for bit_string in bit_strings:
        print(bit_string)
        decode_packet(bit_string, packets)

    version_sum = 0
    for packet in packets:
        print(packet)
        version_sum += packet.version

    print(f"Version sum: {version_sum}")


if __name__ == "__main__":
    main(sys.argv)
