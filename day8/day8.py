class Day8:
    def __init__(self, input_file_name):
        self.input_file_name = input_file_name
        self.read_input_data()
        self.input_data = self.read_input_data()

    def read_input_data(self):
        with open(self.input_file_name) as f:
            data = f.read().splitlines()

        return data

    def count_unique_segments(self):
        count = 0

        for line in self.input_data:
            data = line.split(' | ')
            segments = data[0].split()
            outputs = data[1].split()

            for output in outputs:
                char_len = len(output)

                if char_len == 2 or char_len == 4 or char_len == 3 or char_len == 7:
                    count += 1

        return count

    def sum_outputs(self):
        total_sum = 0
        for line in self.input_data:
            data = line.split(' | ')
            segments = data[0].split()
            outputs = data[1].split()

            finded_segments = self.find_segments(segments)
            print(finded_segments)

            output_numbers = []
            for output in outputs:
                temp = sorted(list(output))
                for index, segment in enumerate(finded_segments):
                    if temp == segment:
                        output_numbers.append(index)
                        break

            final_number = int(''.join(str(e) for e in output_numbers))
            total_sum += final_number
            print(final_number)

        return total_sum



    def find_segments(self, segments):
        # 1, 4, 7, 8 찾기
        for segment in segments:
            if len(segment) == 2:
                number_one = sorted(list(segment))
            if len(segment) == 3:
                number_seven = sorted(list(segment))
            if len(segment) == 4:
                number_four = sorted(list(segment))
            if len(segment) == 7:
                number_eight = sorted(list(segment))

        # print(number_one, number_four, number_seven, number_eight)

        candidate_0_6_9 = []

        for segment in segments:
            if len(segment) == 6:
                candidate_0_6_9.append(segment)

        # 9 찾기
        # 8에서 4와 7을 뺴면  e,g  의 후보가 남는데 0, 6, 9 후보중에서 9 를 제외하고는 e, g 를 둘 다 포함하므로 e, g 를 둘 다 포함하지 않은 것이 9
        number_eight_set = set(number_eight)
        e_g_set = number_eight_set - set(number_four) - set(number_seven)
        # print(e_g_set)
        for candidate in candidate_0_6_9:
            temp = sorted(list(candidate))
            if e_g_set.intersection(temp) != e_g_set:
                number_nine = temp
                candidate_0_6_9.remove(candidate)
                # print(number_nine)
                break

        # 0, 6 찾기
        # 0, 6 중에서 1이 가진 c,f 를 모두 가진 것이 0 아닌 것이 6
        temp1 = set(sorted(list(candidate_0_6_9[0])))
        temp2 = set(sorted(list(candidate_0_6_9[1])))

        number_one_set = set(number_one)
        # print('ok')
        if number_one_set - temp1 == set():
            number_zero = sorted(list(candidate_0_6_9[0]))
            number_six = sorted(list(candidate_0_6_9[1]))
        else:
            number_zero = sorted(list(candidate_0_6_9[1]))
            number_six = sorted(list(candidate_0_6_9[0]))

        # print(number_zero, number_six)

        candidate_2_3_5 = []

        for segment in segments:
            if len(segment) == 5:
                candidate_2_3_5.append(segment)

        number_nine_set = set(number_nine)
        # print(number_nine_set)
        # 2  찾기
        # 2,3,5  와 9를 비교했을 때 2만 9와 3개의 차이점이 발생된다
        for candidate in candidate_2_3_5:
            temp_set = set(sorted(list(candidate)))
            # print(number_nine_set ^ temp_set)
            if len(number_nine_set ^ temp_set) == 3:
                number_two = sorted(list(candidate))
                candidate_2_3_5.remove(candidate)
                break

        # 3, 5  찾기
        # 3, 5  중에서 1이 가진  c, f 를 모두 내포한 것이 3 , 아닌 것이 5


        temp1 = set(sorted(list(candidate_2_3_5[0])))
        temp2 = set(sorted(list(candidate_2_3_5[1])))

        number_one_set = set(number_one)
        # print('ok')
        if number_one_set - temp1 == set():
            number_three = sorted(list(candidate_2_3_5[0]))
            number_five = sorted(list(candidate_2_3_5[1]))
        else:
            number_three = sorted(list(candidate_2_3_5[1]))
            number_five = sorted(list(candidate_2_3_5[0]))

        return [number_zero, number_one, number_two, number_three, number_four, number_five, number_six, number_seven,
              number_eight, number_nine]



