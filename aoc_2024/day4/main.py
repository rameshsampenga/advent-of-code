import os
import re
from functools import reduce

XMAS = "XMAS"
SAMX = "SAMX"

def main():
    # text = open_file(__file__, 'input-sample.txt')
    text = open_file(__file__, 'input-main.txt')
    print(text)

    # part2(text)
    part1(text)

    print()


def part2(text: str):
    lines = list(text.splitlines())
    count_rows = len(lines)
    count_cols = len(lines[0])
    count_x = 0
    for i in range(count_rows - 2):
        for j in range(count_cols - 2):
            if lines[i + 1][j + 1] == "A":
                x1 = lines[i][j] + lines[i + 2][j + 2]
                if x1 == "MS" or x1 == "SM":
                    x2 = lines[i][j + 2] + lines[i + 2][j]
                    if x2 == "MS" or x2 == "SM":
                        count_x += 1
    print(f"count_x = {count_x}")


def part1(text: str):
    rows_f, rows_r = find_all_xmas(text)

    transposed_text = '\n'.join(list(map(lambda x: ''.join(x), list(zip(*text.splitlines())))))
    cols_f, cols_r = find_all_xmas(transposed_text)

    grid = [
        list(line)
        for line in text.strip().splitlines()
    ]
    _len = len(grid)

    diagonal_text = "\n".join(["".join([grid[j][j - i] for j in range(0, i)]) for i in list(range(1, _len + 1))])
    diagonal_text += "\n" + "\n".join(
        ["".join([grid[_len - i + j][j] for j in range(0, i)]) for i in list(range(_len - 1, 0, -1))])
    # print(diagonal_text)
    diag_f, diag_r = find_all_xmas(diagonal_text)

    anti_diagonal_text = "\n".join(
        ["".join([grid[j][i - j - 1] for j in range(0, i)]) for i in list(range(1, _len + 1))])
    anti_diagonal_text += "\n" + "\n".join(
        ["".join([grid[_len - i + j][- j - 1] for j in range(0, i)]) for i in list(range(_len - 1, 0, -1))])
    # print(anti_diagonal_text)
    adiag_f, adiag_r = find_all_xmas(anti_diagonal_text)
    print(
        f"count: {len(rows_f) + len(rows_r) + len(cols_f) + len(cols_r) + len(diag_f) + len(diag_r) + len(adiag_f) + len(adiag_r)}")


def find_all_xmas(text: str):
    count_forward = re.findall(r"%s" % XMAS, text)
    count_reverse = re.findall(r"%s" % SAMX, text)
    return count_forward, count_reverse


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
