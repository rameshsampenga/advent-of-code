import os
from collections import defaultdict
from typing import Any


def main():
    # _input = open_file(__file__, 'input-sample.txt')
    # _input = open_file(__file__, 'input-simple.txt')
    _input = open_file(__file__, 'input-main.txt')
    # print(_input)

    reports = read_input(_input)
    # print(reports)

    part1(reports)
    part2(reports)


def part1(reports: list[list[Any]]):
    safe_reports = 0
    for report in reports:
        safe = is_report_safe(report)
        safe_reports += safe

    print(f"safe_reports: {safe_reports}")

def part2(reports: list[list[Any]]):
    safe_reports = 0
    for report in reports:
        safe = is_report_safe(report)
        index = 0
        while not safe and index < len(report):
            safe = is_report_safe(list_copy_except(index, report))
            index += 1
        safe_reports += safe

    print(f"safe_reports: {safe_reports}")

def is_report_safe(report):
    level_0 = report[0]
    level_p = report[1]
    if level_0 == level_p or abs(level_0 - level_p) > 3:
        return False
    if level_0 > level_p:
        for index, level_n in enumerate(report[2:]):
            if level_n >= level_p or level_p - level_n > 3:
                return False
            level_p = level_n
    if level_0 < level_p:
        for index, level_n in enumerate(report[2:]):
            if level_n <= level_p or level_n - level_p > 3:
                return False
            level_p = level_n
    return True


def list_copy_except(index: int, report) -> Any:
    return report[:index] + report[index + 1:]


def read_input(_input):
    return [
        list(map(int, _list))
        for line in _input.splitlines()
        for _list in [line.split()]
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
