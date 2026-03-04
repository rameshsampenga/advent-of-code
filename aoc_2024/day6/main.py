import os

def main():
    _input = open_file(__file__, 'input-sample.txt')
    # _input = open_file(__file__, 'input-main.txt')
    # print(_input)
    area_map, start_point = read_input(_input)
    start_walking(area_map, start_point, 12)
    count = count_path(area_map)
    print(f"count: {count}")
    print()

def count_path(area_map):
    count = 0
    for row in area_map:
        for cell in row:
            if cell == 'X':
                count += 1
    return count

def start_walking(area_map, start_point, direction):
    direction %= 12
    obstruction, new_start_point = fill_path(area_map, start_point, direction)
    if obstruction:
        start_walking(area_map, new_start_point, direction + 3)  # start walking in 90-degrees


def fill_path(area_map, start_point, direction):
    new_start_point = start_point
    if direction == 0:
        c = start_point[1]
        for r in range(start_point[0], -1, -1):
            if area_map[r][c] != '#':
                area_map[r][c] = 'X'
                new_start_point = r, c
            else:
                return True, new_start_point
    elif direction == 6:
        c = start_point[1]
        for r in range(start_point[0], len(area_map)):
            if area_map[r][c] != '#':
                area_map[r][c] = 'X'
                new_start_point = r, c
            else:
                return True, new_start_point
    elif direction == 3:
        r = start_point[0]
        for c in range(start_point[1], len(area_map)):
            if area_map[r][c] != '#':
                area_map[r][c] = 'X'
                new_start_point = r, c
            else:
                return True, new_start_point
    else:  # direction == 9:
        r = start_point[0]
        for c in range(start_point[1], -1, -1):
            if area_map[r][c] != '#':
                area_map[r][c] = 'X'
                new_start_point = r, c
            else:
                return True, new_start_point
    return False, new_start_point


def read_input(_input: str):
    area_map = []
    start_point = None, None
    for row, line in enumerate(_input.splitlines()):
        l = list(line)
        area_map.append(l)
        if '^' in l:
            start_point = row, l.index('^')
    return area_map, start_point


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
