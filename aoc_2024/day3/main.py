import os
import re
from functools import reduce


def main():
    # _input = open_file(__file__, 'input-sample.txt')
    _input = open_file(__file__, 'input-main.txt')
    print(_input)

    # part1(_input)
    part2(_input)

    print()


def part2(_input: str):
    muls = [
        # match.start() is the start index
        # match.end() is the end index
        # match.group(0) is the full match
        # match.group(1) is the first group
        # match.group(2) is the second group, and so on
        (match.start(), int(match.group(1)) * int(match.group(2)))
        for match in re.finditer(r"mul\((\d+),(\d+)\)", _input)
    ]
    dos = [
        match.start()
        for match in re.finditer(r"do\(\)", _input)
    ]
    donts = [
        match.start()
        for match in re.finditer(r"don't\(\)", _input)
    ]

    print(f"muls:{muls}")
    print(f"dos:{dos}")
    print(f"donts:{donts}")

    do_iter = iter(dos)
    donts_iter = iter(donts)

    next_do = next(do_iter, float('inf'))
    next_dont = next(donts_iter, float('inf'))
    total = 0
    is_do = True
    for mul in muls:
        mul_index = mul[0]
        if mul_index > next_dont:
            if is_do:
                is_do = False
            next_dont = next(donts_iter, float('inf'))
        if mul_index > next_do:
            if not is_do:
                is_do = True
            next_do = next(do_iter, float('inf'))
        if is_do:
            total += mul[1]
            print(f"Adding {mul_index} -> {mul[1]}")
        else:
            print(f"Skipping {mul_index} -> {mul[1]}")

    print(f"total: {total}")


def part1(_input: str):
    matches = re.findall(r"mul\((\d+),(\d+)\)", _input)
    tuples = list(map(lambda match: (int(match[0]), int(match[1])), matches))
    products = map(lambda t: t[0] * t[1], tuples)
    total = reduce(lambda x, y: x + y, products)
    print(f"total:{total}")


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
