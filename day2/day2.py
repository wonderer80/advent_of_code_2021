class Day2:
    def __init__(self, input_file_name):
        self.input_file_name = input_file_name
        self.input_data = self.read_input_data()

    def read_input_data(self):
        with open(self.input_file_name) as f:
            data = f.read().splitlines()

        return data

    def multiply_horizontal_position_by_depth(self):
        horizontal_position = 0
        depth = 0

        for line in self.input_data:
            temp = line.split()
            command = temp[0]
            number = int(temp[1])

            if command == 'forward':
                horizontal_position += number

            if command == 'up':
                depth -= number

            if command == 'down':
                depth += number

        return horizontal_position * depth

    def advenced_multiply_horizontal_position_by_depth(self):
        horizontal_position = 0
        aim = 0
        depth = 0

        for line in self.input_data:
            temp = line.split()
            command = temp[0]
            number = int(temp[1])

            if command == 'forward':
                horizontal_position += number
                depth += aim * number

            if command == 'up':
                aim -= number

            if command == 'down':
                aim += number

        return horizontal_position * depth
