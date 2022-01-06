import copy


class Day6:
    def __init__(self, input_file_name):
        self.init_state = []
        self.init_state2 = []

        self.input_file_name = input_file_name
        self.read_input_data()

    def read_input_data(self):
        with open(self.input_file_name) as f:
            data = f.read().splitlines()

        self.init_state = list(map(int, data[0].split(',')))

        for remain_turn in self.init_state:
            self.init_state2.append({'current_day': 0, 'remain_turn': remain_turn})

    def get_total_lanternfish_count_after_days(self, days):
        current_day = 1
        zero_count = 0

        for i in range(days):
            prev_zero_count = zero_count
            zero_count = 0

            for index, remain_turn in enumerate(self.init_state):
                self.init_state[index] -= 1
                if self.init_state[index] == 0:
                    zero_count += 1
                    self.init_state[index] = 7

            for j in range(prev_zero_count):
                self.init_state.append(8)

            # print(f'days: {current_day}  state: {self.init_state}')
            # print(f'days: {current_day}, count: {len(self.init_state)}')
            current_day += 1

        return len(self.init_state)

    def get_total_lanternfish_count_after_days2(self, days):
        total_count = len(self.init_state2)
        BORN_CYCLE_DAYS = 7

        for state in self.init_state2:
            born_fish_count = int((days-(state['remain_turn']-BORN_CYCLE_DAYS)-(state['current_day']+1))/BORN_CYCLE_DAYS)
            total_count += born_fish_count
            # print(born_fish_count)

            # if state['remain_turn'] < BORN_CYCLE_DAYS:
            #     day = BORN_CYCLE_DAYS - state['remain_turn']
            # else:
            #     day = state['current_day'] + 9

            if state['remain_turn'] == 8:
                day = state['current_day'] + 9
            else:
                day = state['remain_turn']+1

            for i in range(born_fish_count):
                self.init_state2.append({'current_day': day, 'remain_turn': 8})
                day += BORN_CYCLE_DAYS

                # print(total_count)

        return total_count


    def get_total_lanternfish_count_after_days3(self, days):
        fish_dic = {}

        total_count = 0
        num = 5

        init_num = num
        tommorow_fishes = []
        tommorow_fishes.append(init_num)

        for day in range(days+10):
            key = f'num({num}):day{day+1}'
            today_fishes = copy.deepcopy(tommorow_fishes)
            for index, fish in enumerate(today_fishes):
                if fish == 0:
                    tommorow_fishes[index] = 6
                    tommorow_fishes.append(8)
                else:
                    tommorow_fishes[index] -= 1
            print(day, len(tommorow_fishes))
            fish_dic[key] = len(tommorow_fishes)


        print(key, len(tommorow_fishes))

        for input_num in self.init_state:
            key = f'num(5):day{days+(5-input_num)}'

            print(fish_dic[key])
            total_count += fish_dic[key]

        return total_count

    def get_total_lanternfish_count_after_days4(self, days):
        fish_dic = {}

        total_count = 0

        init_num = 10
        tommorow_fishes = []
        tommorow_fishes.append(init_num)

        for day in range(days+10):
            day_x = day+1
            key = f'num({init_num}):day{day_x}'
            today_fishes = copy.deepcopy(tommorow_fishes)
            for index, fish in enumerate(today_fishes):
                if fish == 0:
                    tommorow_fishes[index] = 6
                    tommorow_fishes.append(8)
                else:
                    tommorow_fishes[index] -= 1
            print(day_x, len(tommorow_fishes))
            fish_dic[key] = { 'num': len(tommorow_fishes), 'fishes': copy.deepcopy(tommorow_fishes) }


        # print(key, len(tommorow_fishes))

        for input_num in self.init_state:
            key = f'num({init_num}):day{days+(init_num-input_num)}'

            print(input_num, key, fish_dic[key])
            total_count += fish_dic[key]['num']

        return total_count


    def get_total_lanternfish_count_after_days5(self, days):
        fishes_dict = {}
        current_state = copy.deepcopy(self.init_state)
        for num in current_state:
            if num in fishes_dict:
                fishes_dict[num] += 1
            else:
                fishes_dict[num] = 1

        today_fishes_dict = fishes_dict
        for day in range(days):
            tommorow_fishes_dict = {}
            for number, count in today_fishes_dict.items():
                if number == 0:
                    if 6 in tommorow_fishes_dict:
                        tommorow_fishes_dict[6] += count
                    else:
                        tommorow_fishes_dict[6] = count

                    if 8 in tommorow_fishes_dict:
                        tommorow_fishes_dict[8] += count
                    else:
                        tommorow_fishes_dict[8] = count
                else:
                    tommorow_number = number - 1
                    if tommorow_number in tommorow_fishes_dict:
                        tommorow_fishes_dict[tommorow_number] += count
                    else:
                        tommorow_fishes_dict[tommorow_number] = count

            print(day+1,  tommorow_fishes_dict)
            today_fishes_dict = copy.deepcopy(tommorow_fishes_dict)


        total_count = 0

        for number, count in today_fishes_dict.items():
            total_count += count

        return total_count