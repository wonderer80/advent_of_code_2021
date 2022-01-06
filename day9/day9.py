class Day9:
    def __init__(self, input_file_name):
        self.heightmap = []
        self.input_file_name = input_file_name
        self.input_data = self.read_input_data()
        self.markmap = {}

    def read_input_data(self):
        with open(self.input_file_name) as f:
            data = f.read().splitlines()

        for line in data:
            self.heightmap.append(list(map(int, line)))

        return data

    def sum_risk_level(self):
        total_risk_level = 0
        for y in range(len(self.heightmap)):
            for x in range(len(self.heightmap[0])):
                if self.heightmap[y][x] == 9:
                    continue
                if self.heightmap[y][x] == 0:
                    total_risk_level += 1
                    continue

                left = 999
                right = 999
                top = 999
                bottom = 999

                # left
                if x - 1 >= 0:
                    left = self.heightmap[y][x-1]
                # right
                if x + 1 < len(self.heightmap[0]):
                    right = self.heightmap[y][x+1]
                # top
                if y - 1 >= 0:
                    top = self.heightmap[y-1][x]
                # bottom
                if y + 1 < len(self.heightmap):
                    bottom = self.heightmap[y+1][x]

                if left > self.heightmap[y][x] and right > self.heightmap[y][x] and top > self.heightmap[y][x] and bottom > self.heightmap[y][x]:
                    total_risk_level += (self.heightmap[y][x] + 1)

        return total_risk_level

    def multiply_three_largest_basins(self):
        low_points = self.find_low_points()

        basin_size_list = []
        for low_point in low_points:

            x = low_point[0]
            y = low_point[1]

            basin_size = self.get_basin_size(x, y, 0, None)
            basin_size_list.append(basin_size)

        sorted_basin_size_list = sorted(basin_size_list)

        return sorted_basin_size_list[-1] * sorted_basin_size_list[-2] * sorted_basin_size_list[-3]

    def get_basin_size(self, x, y, basin_size, prev_pos):
        key = f'{x}:{y}'

        if self.heightmap[y][x] == 9 or (key in self.markmap):
            return basin_size

        basin_size = basin_size + 1
        self.markmap[key] = True

        # left
        if x - 1 >= 0 and prev_pos != 'left':
            basin_size = self.get_basin_size(x-1, y, basin_size, 'right')
        # right
        if x + 1 < len(self.heightmap[0]) and prev_pos != 'right':
            basin_size = self.get_basin_size(x+1, y, basin_size, 'left')
        # top
        if y - 1 >= 0 and prev_pos != 'top':
            basin_size = self.get_basin_size(x, y-1, basin_size, 'bottom')
        # bottom
        if y + 1 < len(self.heightmap) and prev_pos != 'bottom':
            basin_size = self.get_basin_size(x, y+1, basin_size, 'top')

        return basin_size

    def find_low_points(self):
        low_points = []

        for y in range(len(self.heightmap)):
            for x in range(len(self.heightmap[0])):
                if self.heightmap[y][x] == 9:
                    continue
                if self.heightmap[y][x] == 0:
                    low_points.append((x,y))
                    continue

                left = 999
                right = 999
                top = 999
                bottom = 999

                # left
                if x - 1 >= 0:
                    left = self.heightmap[y][x-1]
                # right
                if x + 1 < len(self.heightmap[0]):
                    right = self.heightmap[y][x+1]
                # top
                if y - 1 >= 0:
                    top = self.heightmap[y-1][x]
                # bottom
                if y + 1 < len(self.heightmap):
                    bottom = self.heightmap[y+1][x]

                if left > self.heightmap[y][x] and right > self.heightmap[y][x] and top > self.heightmap[y][x] and bottom > self.heightmap[y][x]:
                    low_points.append((x,y))

        return low_points
