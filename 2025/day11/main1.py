import os


def main():
    print("AoC - Day")

    # _input = open_file('input-sample1.txt')
    _input = open_file('input-main.txt')
    print(_input)

    data_map = {}
    for line in _input.splitlines():
        devices = line.split()
        data_map[devices[0].split(':')[0]] = devices[1:]
    print(data_map)

    path_count = number_of_paths(data_map, 'you', 'out')
    print(f"path count {path_count}")
    print()


def number_of_paths(data_map, path_from, path_to):
    path_count = 0
    to_list = data_map[path_from]
    if to_list[0] == 'out':
        path_count += 1
    else:
        for to in to_list:
            path_count += number_of_paths(data_map, to, path_to)

    return path_count


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
