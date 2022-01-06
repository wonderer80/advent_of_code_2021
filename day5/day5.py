class Day5:
    def __init__(self, input_file_name):
        self.vertical_lines = []
        self.horizontal_lines = []
        self.diagonal_lines = []
        self.input_file_name = input_file_name
        self.read_input_data()

    def read_input_data(self):
        with open(self.input_file_name) as f:
            data = f.read().splitlines()

        for line in data:
            points = line.split(' -> ')
            point1 = list(map(int, points[0].split(',')))
            point2 = list(map(int, points[1].split(',')))

            if point1[0] == point2[0]:
                if point1[1] < point2[1]:
                    self.horizontal_lines.append({'x1': point1[0], 'y1': point1[1], 'x2': point2[0], 'y2': point2[1]})
                else:
                    self.horizontal_lines.append({'x1': point2[0], 'y1': point2[1], 'x2': point1[0], 'y2': point1[1]})
            elif point1[1] == point2[1]:
                if point1[0] < point2[0]:
                    self.vertical_lines.append({'x1': point1[0], 'y1': point1[1], 'x2': point2[0], 'y2': point2[1]})
                else:
                    self.vertical_lines.append({'x1': point2[0], 'y1': point2[1], 'x2': point1[0], 'y2': point1[1]})
            else:
                x_distance = abs(point1[0] - point2[0])
                y_distance = abs(point1[1] - point2[1])

                if x_distance == y_distance:
                    if point1[0] < point2[0]:
                        self.diagonal_lines.append(
                            {'x1': point1[0], 'y1': point1[1], 'x2': point2[0], 'y2': point2[1]})
                    else:
                        self.diagonal_lines.append(
                            {'x1': point2[0], 'y1': point2[1], 'x2': point1[0], 'y2': point1[1]})


    def get_overlapped_point_count2(self):
        cross_points = {}

        for vertical_line in self.vertical_lines:
            for x_pos in range(vertical_line['x1'],vertical_line['x2']+1):
                pos_key = f'{x_pos}:{vertical_line["y1"]}'

                if pos_key in cross_points:
                    cross_points[pos_key] += 1
                else:
                    cross_points[pos_key] = 1

        for horizontal_line in self.horizontal_lines:
            for y_pos in range(horizontal_line['y1'],horizontal_line['y2']+1):
                pos_key = f'{horizontal_line["x1"]}:{y_pos}'

                if pos_key in cross_points:
                    cross_points[pos_key] += 1
                else:
                    cross_points[pos_key] = 1

        for diagonal_line in self.diagonal_lines:
            add_key = 1
            y_pos = diagonal_line['y1']

            if diagonal_line['y1'] > diagonal_line['y2']:
                add_key = -1

            for x_pos in range(diagonal_line['x1'],diagonal_line['x2']+1):
                pos_key = f'{x_pos}:{y_pos}'
                y_pos += add_key

                if pos_key in cross_points:
                    cross_points[pos_key] += 1
                else:
                    cross_points[pos_key] = 1

        total_count = 0
        for key, value in cross_points.items():
            if value >= 2:
                total_count += 1

        return total_count

    def get_overlapped_point_count(self):
        cross_points = {}

        for index, vertical_line in enumerate(self.vertical_lines):
            for index2, vertical_line2 in enumerate(self.vertical_lines[index+1:]):
                if vertical_line['y1'] == vertical_line2['y1']:
                    if vertical_line['x1'] <= vertical_line2['x1'] <= vertical_line['x2']:
                        for x_pos in range(vertical_line2['x1'], min(vertical_line['x2'], vertical_line2['x2'])+1):
                            pos_key = f'{x_pos}:{vertical_line["y1"]}'

                            if pos_key in cross_points:
                                cross_points[pos_key] += 1
                            else:
                                cross_points[pos_key] = 1
                    elif vertical_line2['x1'] <= vertical_line['x1'] <= vertical_line2['x2']:
                        for x_pos in range(vertical_line['x1'], min(vertical_line['x2'], vertical_line2['x2'])+1):
                            pos_key = f'{x_pos}:{vertical_line["y1"]}'

                            if pos_key in cross_points:
                                cross_points[pos_key] += 1
                            else:
                                cross_points[pos_key] = 1

        for index, horizontal_line in enumerate(self.horizontal_lines):
            for index2, horizontal_line2 in enumerate(self.horizontal_lines[index+1:]):
                if horizontal_line['x1'] == horizontal_line2['x1']:
                    if horizontal_line['y1'] <= horizontal_line2['y1'] <= horizontal_line['y2']:
                        for y_pos in range(horizontal_line2['y1'], min(horizontal_line['y2'], horizontal_line2['y2'])+1):
                            pos_key = f'{horizontal_line["x1"]}:{y_pos}'

                            if pos_key in cross_points:
                                cross_points[pos_key] += 1
                            else:
                                cross_points[pos_key] = 1
                    elif horizontal_line2['y1'] <= horizontal_line['y1'] <= horizontal_line2['y2']:
                        for y_pos in range(horizontal_line['y1'], min(horizontal_line['y2'], horizontal_line2['y2'])+1):
                            pos_key = f'{horizontal_line["x1"]}:{y_pos}'

                            if pos_key in cross_points:
                                cross_points[pos_key] += 1
                            else:
                                cross_points[pos_key] = 1

        for vertical_line in self.vertical_lines:
            for horizontal_line in self.horizontal_lines:
                if vertical_line['x1'] <= horizontal_line['x1'] <= vertical_line['x2']:
                    if horizontal_line['y1'] <= vertical_line['y1'] <= horizontal_line['y2']:
                        pos_key = f'{horizontal_line["x1"]}:{vertical_line["y1"]}'

                        if pos_key in cross_points:
                            cross_points[pos_key] += 1
                        else:
                            cross_points[pos_key] = 1


        total_count = 0
        for key, value in cross_points.items():
            total_count += value

        return len(cross_points)



