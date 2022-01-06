class Day11:
    def __init__(self, input_file_name):
        self.input_file_name = input_file_name
        self.octopus_map = []
        self.input_data = self.read_input_data()

    def read_input_data(self):
        with open(self.input_file_name) as f:
            data = f.read().splitlines()

        for line in data:
            octopuses = list(map(int, list(line)))
            self.octopus_map.append(octopuses)

        return data

    def total_flashes(self, steps):
        flashed_octopuses = []
        width = len(self.octopus_map[0])
        height = len(self.octopus_map)
        total_flashed_count = 0

        for i in range(steps):
            flashed_count = 0
            for y, octopus_line in enumerate(self.octopus_map):
                for x, octopus in enumerate(octopus_line):
                    self.octopus_map[y][x] += 1
                    if self.octopus_map[y][x] == 10:
                        flashed_octopuses.append((x, y))

            while len(flashed_octopuses) > 0:
                next_flashed_octopuses = []
                for flashed_octopus in flashed_octopuses:
                    x = flashed_octopus[0]
                    y = flashed_octopus[1]

                    self.octopus_map[y][x] = 0
                    flashed_count += 1

                    left_x = x - 1
                    right_x = x + 1
                    top_y = y - 1
                    bottom_y = y + 1

                    # left, top
                    if left_x >= 0 and top_y >= 0:
                        if self.octopus_map[top_y][left_x] != 0:
                            self.octopus_map[top_y][left_x] += 1
                            if self.octopus_map[top_y][left_x] == 10:
                                next_flashed_octopuses.append((left_x, top_y))
                    # top
                    if top_y >= 0:
                        if self.octopus_map[top_y][x] != 0:
                            self.octopus_map[top_y][x] += 1
                            if self.octopus_map[top_y][x] == 10:
                                next_flashed_octopuses.append((x, top_y))

                    # right, top
                    if right_x < width and top_y >= 0:
                        if self.octopus_map[top_y][right_x] != 0:
                            self.octopus_map[top_y][right_x] += 1
                            if self.octopus_map[top_y][right_x] == 10:
                                next_flashed_octopuses.append((right_x, top_y))

                    # left
                    if left_x >= 0:
                        if self.octopus_map[y][left_x] != 0:
                            self.octopus_map[y][left_x] += 1
                            if self.octopus_map[y][left_x] == 10:
                                next_flashed_octopuses.append((left_x, y))

                    # right
                    if right_x < width:
                        if self.octopus_map[y][right_x] != 0:
                            self.octopus_map[y][right_x] += 1
                            if self.octopus_map[y][right_x] == 10:
                                next_flashed_octopuses.append((right_x, y))

                    # left, bottom
                    if left_x >= 0 and bottom_y < height:
                        if self.octopus_map[bottom_y][left_x] != 0:
                            self.octopus_map[bottom_y][left_x] += 1
                            if self.octopus_map[bottom_y][left_x] == 10:
                                next_flashed_octopuses.append((left_x, bottom_y))

                    # bottom
                    if bottom_y < height:
                        if self.octopus_map[bottom_y][x] != 0:
                            self.octopus_map[bottom_y][x] += 1
                            if self.octopus_map[bottom_y][x] == 10:
                                next_flashed_octopuses.append((x, bottom_y))

                    # right, bottom
                    if right_x < width and bottom_y < height:
                        if self.octopus_map[bottom_y][right_x] != 0:
                            self.octopus_map[bottom_y][right_x] += 1
                            if self.octopus_map[bottom_y][right_x] == 10:
                                next_flashed_octopuses.append((right_x, bottom_y))

                flashed_octopuses = next_flashed_octopuses
                # print(flashed_octopuses)
                # print(len(flashed_octopuses))

            total_flashed_count += flashed_count

        return total_flashed_count


    def first_step_which_all_flash(self):
        flashed_octopuses = []
        width = len(self.octopus_map[0])
        height = len(self.octopus_map)
        total_flashed_count = 0

        step = 0
        while True:
            flashed_count = 0
            for y, octopus_line in enumerate(self.octopus_map):
                for x, octopus in enumerate(octopus_line):
                    self.octopus_map[y][x] += 1
                    if self.octopus_map[y][x] == 10:
                        flashed_octopuses.append((x, y))

            while len(flashed_octopuses) > 0:
                next_flashed_octopuses = []
                for flashed_octopus in flashed_octopuses:
                    x = flashed_octopus[0]
                    y = flashed_octopus[1]

                    self.octopus_map[y][x] = 0
                    flashed_count += 1

                    left_x = x - 1
                    right_x = x + 1
                    top_y = y - 1
                    bottom_y = y + 1

                    # left, top
                    if left_x >= 0 and top_y >= 0:
                        if self.octopus_map[top_y][left_x] != 0:
                            self.octopus_map[top_y][left_x] += 1
                            if self.octopus_map[top_y][left_x] == 10:
                                next_flashed_octopuses.append((left_x, top_y))
                    # top
                    if top_y >= 0:
                        if self.octopus_map[top_y][x] != 0:
                            self.octopus_map[top_y][x] += 1
                            if self.octopus_map[top_y][x] == 10:
                                next_flashed_octopuses.append((x, top_y))

                    # right, top
                    if right_x < width and top_y >= 0:
                        if self.octopus_map[top_y][right_x] != 0:
                            self.octopus_map[top_y][right_x] += 1
                            if self.octopus_map[top_y][right_x] == 10:
                                next_flashed_octopuses.append((right_x, top_y))

                    # left
                    if left_x >= 0:
                        if self.octopus_map[y][left_x] != 0:
                            self.octopus_map[y][left_x] += 1
                            if self.octopus_map[y][left_x] == 10:
                                next_flashed_octopuses.append((left_x, y))

                    # right
                    if right_x < width:
                        if self.octopus_map[y][right_x] != 0:
                            self.octopus_map[y][right_x] += 1
                            if self.octopus_map[y][right_x] == 10:
                                next_flashed_octopuses.append((right_x, y))

                    # left, bottom
                    if left_x >= 0 and bottom_y < height:
                        if self.octopus_map[bottom_y][left_x] != 0:
                            self.octopus_map[bottom_y][left_x] += 1
                            if self.octopus_map[bottom_y][left_x] == 10:
                                next_flashed_octopuses.append((left_x, bottom_y))

                    # bottom
                    if bottom_y < height:
                        if self.octopus_map[bottom_y][x] != 0:
                            self.octopus_map[bottom_y][x] += 1
                            if self.octopus_map[bottom_y][x] == 10:
                                next_flashed_octopuses.append((x, bottom_y))

                    # right, bottom
                    if right_x < width and bottom_y < height:
                        if self.octopus_map[bottom_y][right_x] != 0:
                            self.octopus_map[bottom_y][right_x] += 1
                            if self.octopus_map[bottom_y][right_x] == 10:
                                next_flashed_octopuses.append((right_x, bottom_y))

                flashed_octopuses = next_flashed_octopuses
                # print(flashed_octopuses)
                # print(len(flashed_octopuses))

            total_flashed_count += flashed_count
            step += 1

            # print(flashed_count)
            if flashed_count == (width*height):
                break

        return step
