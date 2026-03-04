import os
from math import prod


def main():
    print("AoC - Day")

    # _input = open_file('input-simple.txt')
    # _input = open_file('input-sample.txt')
    # _input = open_file('input-main.txt')
    # print(_input)

    with open(get_file_path("input-sample.txt")) as f:
        data = f.read().strip()

    res = 0
    for l in data.split("\n\n")[-1].split("\n"):
        rxc, *nums = l.split()
        _product = prod(map(int, rxc[:-1].split("x")))
        _sum = sum(map(int, nums))
        res += _product >= 7 * _sum

    print(res)


def open_file(filename):
    file_path = get_file_path(filename)

    try:
        with open(file_path, 'r') as file:
            content = file.read()
            return content
    except FileNotFoundError:
        return "File not found."
    except Exception as e:
        return str(e)

def get_file_path(filename):
    current_dir = os.path.dirname(os.path.abspath(__file__))
    file_path = os.path.join(current_dir, filename)
    return file_path


main()
