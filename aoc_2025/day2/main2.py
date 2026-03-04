# Example: 9354772901 - 10 digits
# loop from 1 to half of the digits
# 1 digit sequences - take 1 digit ; compare with next 1 digit  and so on till the end
# 2 digit sequences - take 2 digits; compare with next 2 digits and so on till the end (only when the digits are divisible by 2)
# 3 digit sequences - take 3 digits; compare with next 3 digits and so on till the end (only when the digits are divisible by 3)
# 4 digit sequences - take 4 digits; compare with next 4 digits and so on till the end (only when the digits are divisible by 4)
# 5 digit sequences - take 5 digits; compare with next 5 digits and so on till the end (only when the digits are divisible by 5)

import os
import re


def main():
    print("AoC - Day2b")

    # _input = open_file('input-simple.txt')
    # _input = open_file('input-sample.txt')
    _input = open_file('input-main.txt')
    print(_input)
    sum_of_invalid_ids = 0

    ranges = [
        range(int(_from), int(_to) + 1)
        for range_str in _input.split(',')
        for _from, _to in [range_str.split('-')]
    ]

    for _range in ranges:
        # print()
        # print(f"[DEBUG] 1. Range {_range}")

        invalid_ids = set()
        for product_id in _range:
            product_id_str = str(product_id)
            id_length = len(product_id_str)
            # print(f"  [DEBUG] 2. Prod-ID {product_id_str} {{{id_length}}}")

            for id_seq_length in range(1, (id_length // 2) + 1):
                id_seqs = split_by_regex(product_id_str, id_seq_length)
                matched = check_all_equal(id_seqs)
                # print(f"    [DEBUG] 3. ID-Seq {id_seqs}; Matched? {matched}")

                if matched:
                    invalid_ids.add(product_id)
        sum_of_invalid_ids += sum(invalid_ids)
        print(f"{_range} has {len(invalid_ids)} invalid IDs, {invalid_ids}.")
    print()
    print(f"Adding up all the invalid IDs produces {sum_of_invalid_ids}.")


# def check_all_equal(arr):
#     first_element = arr[0]
#     return all(x == first_element for x in arr)

def check_all_equal(arr):
    return len(set(arr)) == 1


def split_by_regex(s, chunk_size):
    expr = f'.{{{chunk_size}}}|.+'
    return re.findall(expr, s)


def open_file(filename):
    # current_dir = os.getcwd()
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
