import os

def main():
    print("AoC - Day5a")

    # _input = open_file('input-sample.txt')
    _input = open_file('input-main.txt')
    # print(_input)
    splitlines = _input.splitlines()
    blank_index = splitlines.index("")
    fresh_id_ranges = [
        range(int(_from), int(_to) + 1)
        for range_str in splitlines[:blank_index]
        for _from, _to in [range_str.split("-")]
    ]
    ingredient_ids = [int(_num) for _num in splitlines[blank_index + 1:]]

    # print(f"DEBUG: fresh_id_ranges = {fresh_id_ranges}")
    # print(f"DEBUG: ingredient_ids = {ingredient_ids}")

    fresh_ingredient_ids = 0
    for ingredient_id in ingredient_ids:
        is_fresh, _range = find_number(ingredient_id, fresh_id_ranges)
        if is_fresh:
            print(f"Ingredient ID {ingredient_id} is fresh, from {_range}.")
            fresh_ingredient_ids = fresh_ingredient_ids + 1
    print(f"available ingredient IDs: {fresh_ingredient_ids}")


def find_number(number, ranges):
    for _range in ranges:
        if number in _range:
            return True, _range
    return False, None

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
