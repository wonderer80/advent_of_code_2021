import copy

from array import array


class Day3:
    def __init__(self, input_file_name):
        self.input_file_name = input_file_name
        self.input_data = self.read_input_data()
        self.bit_width = len(self.input_data[0])

    def read_input_data(self):
        with open(self.input_file_name) as f:
            data = f.read().splitlines()

        return data

    def get_power_consumption(self):
        bit_count = array('i')

        for i in range(self.bit_width):
            bit_count.append(0)

        for bits in self.input_data:
            for idx, bit in enumerate(list(bits)):
                if bit == '0':
                    bit_count[idx] -= 1
                elif bit == '1':
                    bit_count[idx] += 1

        print(bit_count)

        for i in range(self.bit_width):
            if bit_count[i] > 0:
                bit_count[i] = 1
            elif bit_count[i] < 0:
                bit_count[i] = 0

        print(bit_count)

        gamma_rate = self.arr_to_binary(bit_count)
        print(gamma_rate)
        epsilon_rate = self.reverse_bits(gamma_rate)
        print(epsilon_rate)

        return int(gamma_rate, 2) * int(epsilon_rate, 2)

    def get_life_support_rating(self):
        filtered_data = copy.deepcopy(self.input_data)
        print(filtered_data)

        idx = 0
        oxygen_rating = self.find_rating(filtered_data, idx, 'oxygen')
        scrubber_rating = self.find_rating(filtered_data, idx, 'scrubber')

        print(oxygen_rating)
        print(scrubber_rating)

        return int(oxygen_rating, 2) * int(scrubber_rating, 2)

    def find_rating(self, origin_data, idx, rating_type):
        bit_count = 0

        if len(origin_data) == 1:
            return origin_data[0]

        if rating_type == 'oxygen':
            representative_char = '1'
        elif rating_type == 'scrubber':
            representative_char = '0'

        for bits in origin_data:
            temp = list(bits)
            bit = temp[idx]

            if bit == representative_char:
                bit_count += 1
            else:
                bit_count -= 1

        if bit_count > 0:
            filtered_data = self.filter_data(origin_data, idx, '1')
        elif bit_count < 1:
            filtered_data = self.filter_data(origin_data, idx, '0')
        if bit_count == 0:
            filtered_data = self.filter_data(origin_data, idx, representative_char)

        idx += 1
        print(idx, filtered_data)


        return self.find_rating(filtered_data, idx, rating_type)

    def filter_data(self, origin_data, idx, filter_char):
        filtered_data = []

        for bits in origin_data:
            if bits[idx] == filter_char:
                filtered_data.append(bits)

        return filtered_data

    def arr_to_binary(self, arr):
        temp = [str(i) for i in arr]

        return "".join(temp)

    def reverse_bits(self, bits):
        reversed_bits = []

        for idx, bit in enumerate(list(bits)):
            if bit == '0':
                reversed_bits.append('1')
            elif bit == '1':
                reversed_bits.append('0')

        return self.arr_to_binary(reversed_bits)
