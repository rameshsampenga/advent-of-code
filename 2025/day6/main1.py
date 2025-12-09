import os

def main():
    print("AoC - Day2")

    # _input = open_file('input-sample.txt')
    _input = open_file('input-main.txt')
    print(_input)

    splitlines = _input.splitlines()
    count_of_lines = len(splitlines)
    numbers = []
    operators = []
    for index, line in enumerate(splitlines):
        if index == count_of_lines -1:
            operators = line.split()
        else:
            numbers.append([int(w) for w in line.split()])
    print(f"numbers: {numbers}")

    transposed_numbers = [list(column) for column in zip(*numbers)]
    print(f"numbers: {transposed_numbers}")

    print(f"operators: {operators}")

    print("-"*50)
    total = 0
    for index, operator in enumerate(operators):
        if operator == '*':
            sub_total = 1
            for number in transposed_numbers[index]:
                sub_total = sub_total * number
            total = total + sub_total
        if operator == '+':
            sub_total = 0
            for number in transposed_numbers[index]:
                sub_total = sub_total + number
            total = total + sub_total
    print(f"total = {total}")


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
