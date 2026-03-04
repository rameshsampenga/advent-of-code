import os


def main():
    print("AoC - Day5b")

    # _input = open_file('input-simple.txt')
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

    print(f"fresh-id-ranges: {fresh_id_ranges}")
    # sorted_fresh_id_ranges = sorted(fresh_id_ranges, key=lambda x: (x[0], x[1]))
    # print(f"sorted-fresh-id-ranges: {sorted_fresh_id_ranges}")

    current_id_ranges = fresh_id_ranges
    while True:
        merged_id_ranges = []
        for fresh_id_range in current_id_ranges:
            print(f"processing: {fresh_id_range}")
            check_n_merge(fresh_id_range, merged_id_ranges)
        print(f"merged-ranges: {len(merged_id_ranges)}; current-ranges: {len(current_id_ranges)}")
        if len(merged_id_ranges) < len(current_id_ranges):
            current_id_ranges = merged_id_ranges
        else:
            break

    print(f"current_id_ranges: {current_id_ranges}")

    total_fresh_ingredients = 0
    for fresh_id_range in current_id_ranges:
        total_fresh_ingredients = total_fresh_ingredients + len(fresh_id_range)

    print(f"total fresh ID ranges = {total_fresh_ingredients}")


def check_n_merge(fresh_id_range, merged_id_ranges):
    for index, id_range in enumerate(merged_id_ranges):
        i_min, i_max = id_range[0], id_range[-1]
        validate_range(i_min, i_max)

        _min, _max = fresh_id_range[0], fresh_id_range[-1]
        validate_range(_min, _max)

        if i_min <= _min <= i_max:
            max_ = i_max if i_max > _max else _max
            merged_id_ranges[index] = range(i_min, max_ + 1)
            return
        if i_min <= _max <= i_max:
            min_ = i_min if i_min < _min else _min
            merged_id_ranges[index] = range(min_, i_max + 1)
            return
        if _min <= i_min and _max >= i_max:
            merged_id_ranges[index] = fresh_id_range
        if i_min <= _min and i_max >= _max:
            return

    merged_id_ranges.append(fresh_id_range)


def validate_range(_min, _max):
    if _max < _min:
        raise ValueError(f"max:'{_max}' cannot be less than min:'{_min}'")


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
