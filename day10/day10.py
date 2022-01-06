class Day10:
    def __init__(self, input_file_name):
        self.heightmap = []
        self.input_file_name = input_file_name
        self.input_data = self.read_input_data()

    def read_input_data(self):
        with open(self.input_file_name) as f:
            data = f.read().splitlines()

        return data

    def total_syntax_error_score(self):
        incorrect_chunks = []
        for line in self.input_data:
            open_chunks = []
            for chunk in list(line):
                if chunk in ['[', '(', '{', '<']:
                    open_chunks.append(chunk)
                else:
                    if open_chunks[-1] == '(':
                        if chunk != ')':
                            incorrect_chunks.append(chunk)
                            break
                    elif open_chunks[-1] == '[':
                        if chunk != ']':
                            incorrect_chunks.append(chunk)
                            break
                    elif open_chunks[-1] == '{':
                        if chunk != '}':
                            incorrect_chunks.append(chunk)
                            break
                    elif open_chunks[-1] == '<':
                        if chunk != '>':
                            incorrect_chunks.append(chunk)
                            break
                    open_chunks.pop()

        print(incorrect_chunks)
        total_score = 0
        for incorrect_chunk in incorrect_chunks:
            if incorrect_chunk == ')':
               total_score += 3
            if incorrect_chunk == ']':
                total_score += 57
            if incorrect_chunk == '}':
                total_score += 1197
            if incorrect_chunk == '>':
                total_score += 25137

        return total_score

    def middle_score(self):
        total_scores = []
        for line in self.input_data:
            open_chunks = []
            is_incorrected_line = False
            for chunk in list(line):
                if chunk in ['[', '(', '{', '<']:
                    open_chunks.append(chunk)
                else:
                    if open_chunks[-1] == '(':
                        if chunk != ')':
                            is_incorrected_line = True
                            break
                    elif open_chunks[-1] == '[':
                        if chunk != ']':
                            is_incorrected_line = True
                            break
                    elif open_chunks[-1] == '{':
                        if chunk != '}':
                            is_incorrected_line = True
                            break
                    elif open_chunks[-1] == '<':
                        if chunk != '>':
                            is_incorrected_line = True
                            break
                    open_chunks.pop()
            # print(open_chunks)

            if is_incorrected_line:
                continue

            close_chunks = []
            for open_chunk in reversed(open_chunks):
                if open_chunk == '(':
                    close_chunks.append(')')
                elif open_chunk == '[':
                    close_chunks.append(']')
                elif open_chunk == '{':
                    close_chunks.append('}')
                elif open_chunk == '<':
                    close_chunks.append('>')

            print(close_chunks)
            total_score = 0
            prev_score = 0

            for close_chunk in close_chunks:
                score = 0

                if close_chunk == ')':
                    score = 1
                if close_chunk == ']':
                    score = 2
                if close_chunk == '}':
                    score = 3
                if close_chunk == '>':
                    score = 4

                total_score = (total_score * 5) + score

            total_scores.append(total_score)



        sorted_total_scores = sorted(total_scores)
        middle_index = int(len(total_scores)/2)

        return sorted_total_scores[middle_index]