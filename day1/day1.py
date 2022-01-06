class Day1:
    def __init__(self, input_file_name):
        self.input_file_name = input_file_name
        self.input_data = self.read_input_data()

    def read_input_data(self):
        with open(self.input_file_name) as f:
            data = list(map(int, f.read().splitlines()))

        return data

    def count_increments(self):
        previous_depth = None
        total_count = 0
        for idx, current_depth in enumerate(self.input_data):
            if previous_depth is not None and current_depth > previous_depth:
                total_count += 1
            previous_depth = current_depth

        return total_count

    def count_incremental_sums(self, window_num):
        previous_sum = None
        total_count = 0
        idx = 0

        while idx <= len(self.input_data) - window_num:
            current_sum = 0

            for i in range(3):
                current_sum += self.input_data[idx+i]

            if previous_sum is not None and previous_sum < current_sum:
                total_count += 1

            previous_sum = current_sum
            idx += 1

        return total_count
