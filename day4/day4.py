class Day4:
    def __init__(self, input_file_name):
        self.draw_numbers = None
        self.boards = []
        self.input_file_name = input_file_name
        self.read_input_data()

    def read_input_data(self):
        with open(self.input_file_name) as f:
            data = f.read().splitlines()

        self.draw_numbers = map(int, data[0].split(','))
        # print(self.draw_numbers)

        board = Board()
        self.boards.append(board)
        for line in data[2:]:
            # print(line)
            if line != '':
                row = []
                row.append(line[0:2])
                row.append(line[3:5])
                row.append(line[6:8])
                row.append(line[9:11])
                row.append(line[12:15])

                board.add_row(row)
            else:
                board = Board()
                self.boards.append(board)

        # print(self.boards)

    def first_bingo_final_score(self):
        for number in self.draw_numbers:
            print(number)
            for board in self.boards:
                if board.check_bingo(number):
                    return board.sum_unmarked_number() * number

    def last_bingo_final_score(self):
        bingo_count = 0

        for number in self.draw_numbers:
            print(number)
            for board in self.boards:
                if board.is_bingo:
                    continue

                if board.check_bingo(number):
                    bingo_count += 1
                    if bingo_count == len(self.boards):
                        return board.sum_unmarked_number() * number


class Board:
    def __init__(self):
        self.rows = []
        self.is_bingo = False

    def add_row(self, row):
        row_info = []
        row_info.append({'number': int(row[0].strip()), 'is_matched': False})
        row_info.append({'number': int(row[1].strip()), 'is_matched': False})
        row_info.append({'number': int(row[2].strip()), 'is_matched': False})
        row_info.append({'number': int(row[3].strip()), 'is_matched': False})
        row_info.append({'number': int(row[4].strip()), 'is_matched': False})

        self.rows.append(row_info)

    def check_bingo(self, number):
        # marking number
        pos = self.search_number_position(number)

        if not pos:
            return False

        self.rows[pos['y']][pos['x']]['is_matched'] = True
        # print(self.rows[pos['y']][pos['x']])
        print(pos)
        # check bingo

        # check row
        row_bingo = True
        for x in range(5):
            # print(self.rows[pos['y']][x])
            if not self.rows[pos['y']][x]['is_matched']:
                row_bingo = False
                break

        if row_bingo:
            self.is_bingo = True
            return True

        # check column
        column_bingo = True
        for y in range(5):
            # print(self.rows[y][pos['x']])
            if not self.rows[y][pos['x']]['is_matched']:
                column_bingo = False
                break

        if column_bingo:
            self.is_bingo = True
            return True

        return False

    def search_number_position(self, number):
        for y in range(5):
            for x in range(5):
                # print(self.rows[y][x])
                if self.rows[y][x]['number'] == number:
                    return {'x': x, 'y': y}

    def sum_unmarked_number(self):
        total = 0

        for row in self.rows:
            for i in range(5):
                if not row[i]['is_matched']:
                    total += row[i]['number']

        return total