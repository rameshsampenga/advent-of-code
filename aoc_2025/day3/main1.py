import os


def main():
    print("AoC - Day3a")

    # _input = open_file('input-simple.txt')
    _input = open_file('input-sample.txt')
    # _input = open_file('input-main.txt')
    print(_input)

    total_joltage = 0
    for line in _input.splitlines():
        # print("---------")

        joltages = [int(char) for char in line]
        # print(joltages)

        first_max_joltage = max(joltages[0:-1])
        first_max_joltage_index = joltages.index(first_max_joltage)

        # print(joltages[first_max_joltage_index+1:])
        seond_max_joltage = max(joltages[first_max_joltage_index + 1:])
        # seond_max_joltage_index = joltages.index(seond_max_joltage)

        max_joltage = first_max_joltage * 10 + seond_max_joltage
        total_joltage = total_joltage + max_joltage
        print(f"In {line}, largest joltage possible is {max_joltage}")

    print(f"total output joltage is {total_joltage}")


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
