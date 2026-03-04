import os


def main():
    print("AoC - Day2a")

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

        invalid_ids = []
        for product_id in _range:
            product_id_str = str(product_id)
            id_length = len(product_id_str)
            if id_length % 2 == 0:
                midpoint = id_length // 2
                id_first_half = product_id_str[:midpoint]
                id_second_half = product_id_str[midpoint:]

                if id_first_half == id_second_half:
                    invalid_ids.append(product_id)
                    sum_of_invalid_ids += product_id
        print(f"{_range} has {len(invalid_ids)} invalid IDs, {invalid_ids}.")
    print(f"Adding up all the invalid IDs produces {sum_of_invalid_ids}.")


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
