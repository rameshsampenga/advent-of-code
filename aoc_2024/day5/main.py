import os
from collections import defaultdict
from typing import Any


def main():
    _input = open_file(__file__, 'input-sample.txt')
    # _input = open_file(__file__, 'input-main.txt')
    # print(_input)

    rules_before, rules_after, updates = read_input(_input)
    print(f"count of all updates: {len(updates)}")

    valid_updates = []
    invalid_updates = []
    for print_order in updates:
        valid = make_valid_print_order(print_order, rules_after, rules_before)
        if valid:
            valid_updates.append(print_order)
        else:
            invalid_updates.append(print_order)
    print(f"count of valid updates: {len(valid_updates)}")
    print(f"count of invalid updates: {len(invalid_updates)}")
    print(f"sum middle pages of valid updates: {sum_of_middle_pages(valid_updates)}")
    print(f"sum middle pages of invalid updates: {sum_of_middle_pages(invalid_updates)}")
    print()

def make_valid_print_order(print_order: list[int], rules_after: defaultdict[int, list], rules_before: defaultdict[int, list]) -> bool:
    valid = True
    for index, page in enumerate(print_order):
        before_list = print_order[:index]
        after_list = print_order[index + 1:]
        valid_before, fault_before = validate_before_list(before_list, rules_after[page])
        valid_after, fault_after = validate_after_list(after_list, rules_before[page])
        valid = valid_before and valid_after
        if not valid:
            faulty_index = print_order.index(fault_after)
            print_order[index], print_order[faulty_index] = print_order[faulty_index], print_order[index]
            make_valid_print_order(print_order, rules_after, rules_before)
            break
    return valid


def sum_of_middle_pages(valid_updates: list[Any]) -> int:
    sum_middle_pages = 0
    for pages in valid_updates:
        sum_middle_pages += pages[len(pages) // 2]
    return sum_middle_pages


def validate_before_list(before_list, after_rules):
    for before in before_list:
        if before in after_rules:
            return False, before
    return True, None


def validate_after_list(after_list, before_rules):
    for after in after_list:
        if after in before_rules:
            return False, after
    return True, None


def read_input(_input: str):
    input1, input2 = _input.split("\n\n")
    rules_after = defaultdict(list)
    rules_before = defaultdict(list)
    for line in input1.splitlines():
        x, y = [int(n) for n in line.split('|')]
        rules_after[x].append(y)
        rules_before[y].append(x)
    updates = [
        list(map(int, nums))
        for line in input2.splitlines()
        for nums in [line.split(',')]
    ]
    return rules_before, rules_after, updates


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
