import os
from collections import defaultdict

def main():
    # _input = open_file(__file__, 'input-sample.txt')
    _input = open_file(__file__, 'input-main.txt')
    # print(_input)

    input_pairs = read_input(_input)
    print(_input)

    list1, list2 = map(list, zip(*input_pairs))
    # part1(list1, list2)
    part2(list1, list2)

    print()


def part2(list1, list2):
    # Automatically creates [] for new keys
    D = defaultdict(int)
    for n in list2:
        D[n] += 1

    score = 0
    for n in list1:
        score += n * D[n]
    print(f"score: {score}")

def part1(list1, list2):
    list1 = sorted(list1)
    list2 = sorted(list2)
    total_distance = 0
    for pair in zip(list1, list2):
        total_distance += abs(pair[0] - pair[1])
    print(f"total_distance: {total_distance}")


def read_input(_input):
    return [
        (int(x), int(y))
        for line in _input.splitlines()
        for x,y in [line.split()]
    ]

def open_file(path, filename):
    current_dir = os.path.dirname(os.path.abspath(path))
    file_path = os.path.join(current_dir, filename)

    try:
        with open(file_path, 'r') as file:
            content = file.read()
            return content
    except FileNotFoundError:
        return "File not found."
    except Exception as e:
        return str(e)

if __name__ == '__main__':
    main()
