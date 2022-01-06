class Day7:
    def __init__(self, input_file_name):
        self.input_file_name = input_file_name
        self.crab_positions = {}
        self.read_input_data()

    def read_input_data(self):
        with open(self.input_file_name) as f:
            data = f.read().split(',')

        for position in data:
            if position in self.crab_positions:
                self.crab_positions[position]['count'] += 1
            else:
                self.crab_positions[position] = {'count': 1}

    def min_fuel_for_alingn(self):
        # print(self.crab_positions)

        crab_position_list = list(self.crab_positions.items())

        for index, (number, contents) in enumerate(crab_position_list):
            # print(f'align number: {number}')
            contents['total_fuel'] = 0
            for index2, (number2, contents2) in enumerate(crab_position_list):
                if index == index2:
                    continue
                distance = abs(int(number) - int(number2))
                fuel = distance * contents2['count']
                contents['total_fuel'] += fuel

            # print(contents['total_fuel'])

        # print(crab_position_list)

        min_fuel = 9999999999
        aligned_position = None
        for index, (number, contents) in enumerate(crab_position_list):
            if min_fuel > contents['total_fuel']:
                aligned_position = index
                min_fuel = contents['total_fuel']

        print(crab_position_list[aligned_position])

        return crab_position_list[aligned_position][1]['total_fuel']


    def min_fuel_for_alingn2(self):

        keys = sorted(map(int, list(self.crab_positions.keys())))
        min = keys[0]
        max = keys[-1]

        print(keys)
        print(min, max)

        total_fuel = {}

        for position in range(min, max+1):
            crab_position_list = list(self.crab_positions.items())

            for index, (number, contents) in enumerate(crab_position_list):
                distance = abs(position-int(number))
                if distance == 0:
                    continue

                if distance%2==0:
                    fuel = (1+distance)*int(distance/2) * contents['count']
                else:
                    fuel = ((1+distance)*int(distance/2) + int(distance/2) + 1) * contents['count']

                if position in total_fuel:
                    total_fuel[position] += fuel
                else:
                    total_fuel[position] = fuel


        min_fuel = 100000000
        min_position = None

        for key, value in total_fuel.items():
            if min_fuel > value:
                min_fuel = value
                min_position = key

        return min_fuel




