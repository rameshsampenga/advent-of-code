import os

def main():
    print("AoC - Day3b")

    # _input = open_file('input-simple.txt')
    # _input = open_file('input-sample.txt')
    _input = open_file('input-main.txt')
    # print(_input)

    total_joltage = 0
    number_of_batteries = 12
    for line in _input.splitlines():
        # print("---------")

        joltages = [int(char) for char in line]
        bank_length = len(joltages)
        # print(joltages)
        joltages_sequence_int = []
        start_index = 0
        for idx in range(number_of_batteries,0,-1):
            end_index = bank_length-(idx - 1)
            joltages_splice = joltages[start_index:end_index]
            # print(f"Index-{idx}: {joltages_splice}")

            max_joltage_value, max_joltage_index = max_value(joltages_splice)
            start_index = start_index + max_joltage_index + 1
            joltages_sequence_int.append(max_joltage_value)
            # print(f"{max_joltage_value} at {max_joltage_index}, Next start at: {start_index}, Seq: {joltages_sequence_int}")


        joltages_sequence_char = (str(i) for i in joltages_sequence_int)
        joltages_sequence = "".join(joltages_sequence_char)
        max_bank_joltage = int(joltages_sequence)

        total_joltage = total_joltage + max_bank_joltage
        print(f"In {line}, largest joltage possible is {max_bank_joltage}")

    print(f"total output joltage is {total_joltage}")


def max_value(ints: list[int]) -> tuple[int, int]:
    max_value = max(ints)
    max_index = ints.index(max_value)
    return max_value, max_index


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
