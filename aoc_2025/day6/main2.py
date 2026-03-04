import os


def main():
    print("AoC - Day2")

    # _input = open_file('input-sample.txt')
    _input = open_file('input-main.txt')
    print(_input)

    splitlines = _input.splitlines()
    count_of_lines = len(splitlines)

    digit_count = []
    chars = list(splitlines[-1])
    line_length = len(chars)
    index = 0
    count = 0
    operators = []
    while index < line_length:
        char = chars[index]
        if char == '*' or char == '+' or char == '|':
            if char != '|': operators.append(char)
            if count != 0:
                digit_count.append(count if char == '|' else count - 1)
                count = 0
            count = count + 1
        else:  # space
            count = count + 1
        index = index + 1

    print(f"digit_count: {digit_count}")

    operator_i = 0
    numbers = []
    number_chars = []
    total = 0
    for char_i in range(line_length - 1):
        for line_i in range(0, count_of_lines - 1):
            number_chars.append(splitlines[line_i][char_i])
        number_str = "".join(number_chars).strip()
        if len(number_str) != 0:
            numbers.append(int(number_str))
            number_chars = []
        else:
            sub_total = calculate(operators[operator_i], numbers)
            total = total + sub_total
            print(f"sub_total = {sub_total}")
            numbers = []
            operator_i = operator_i + 1
    sub_total = calculate(operators[operator_i], numbers)
    total = total + sub_total
    print(f"sub_total = {sub_total}")
    print(f"total = {total}")


def calculate(operator, numbers):
    total = 0
    if operator == '*':
        total = 1
        for number in numbers:
            total = total * number

    if operator == '+':
        total = 0
        for number in numbers:
            total = total + number
    return total


def open_file(filename):
    current_dir = os.path.dirname(os.path.abspath(__file__))
    file_path = os.path.join(current_dir, filename)

    try:
        with open(file_path, 'r') as file:
            content = file.read()
            return content
    except FileNotFoundError:
        return "File not found."
    except Exception as e:
        return str(e)


main()
