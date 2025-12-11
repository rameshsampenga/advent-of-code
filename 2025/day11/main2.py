import os
from typing import Any


def main():
    print("AoC - Day11")

    # _input = open_file('input-sample2.txt')
    _input = open_file('input-main.txt')
    print(_input)

    data_map = {}
    for line in _input.splitlines():
        devices = line.split()
        data_map[devices[0].split(':')[0]] = devices[1:]
    print(data_map)

    path_count = dict_paths_count(data_map, 'svr')
    print(f"path_count {path_count}")
    print()


def dict_paths_count(data_map, device_start):
    count_map = {}

    def dfs(node):
        if count_map.get(node) is not None:
            return count_map.get(node)
        if node == 'out':
            return {'': 1}  # device_map
        else:
            device_map = {}
            for child in data_map[node]:
                device_map_child = dfs(child)
                merge_device_map(device_map, device_map_child)
            if node == 'fft' or node == 'dac':
                update_device_map(node, device_map)
        count_map[node] = device_map
        return device_map

    def update_device_map(key, device_map: dict[Any, Any]):
        if device_map.get('') is not None:
            device_map[key] = device_map.get('')
            device_map.pop('')
        alt_key = 'dac' if key == 'fft' else 'fft'
        if device_map.get(alt_key) is not None:
            device_map['dac+fft'] = device_map.get(alt_key)
            device_map.pop(alt_key)

    def merge_device_map(device_map, child_device_map):
        for key in child_device_map.keys():
            if key in device_map:
                device_map[key] += child_device_map[key]
            else:
                device_map[key] = child_device_map[key]

    root_device_map = dfs(device_start)
    return root_device_map

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
