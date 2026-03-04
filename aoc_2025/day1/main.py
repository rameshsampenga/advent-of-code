import os


def main():
    print("AoC - Day1")

    # _input = open_file('input-sample.txt')
    _input = open_file('input-main.txt')
    # print(_input)

    dial_start = 50
    dial_at = dial_start
    dial_zero_at_end = 0
    dial_zero_during_total = 0

    print(f"The dial starts by pointing at {dial_start}.")

    for line in _input.splitlines():

        direction = line[0]
        clicks = int(line[1:])

        dial_zero_during_old = dial_zero_during_total

        dial_zero_during = clicks // 100
        clicks = clicks % 100

        dial_at = dial_at + clicks if direction == 'R' else dial_at - clicks

        if dial_at > 100:
            dial_at -= 100
            dial_zero_during += 1

        dial_at = 0 if dial_at == 100 else dial_at

        if dial_at < 0:
            if dial_at + clicks != 0:
                dial_zero_during += 1
            dial_at += 100

        dial_zero_at_end += 1 if dial_at == 0 else 0
        dial_zero_during_total += dial_zero_during

        message = f"The dial is rotated {clicks}/{line} to point at {dial_at}"
        message = message + f"; during this rotation, it points at 0 -> {dial_zero_during} time(s)" if dial_zero_during_old != dial_zero_during_total else message + "."
        # print(message) # DEBUG

    print()
    print(f"the password at 1st door is: {dial_zero_at_end}")
    print(
        f"the dial points at 0 -> {dial_zero_at_end} times at the end of a rotation, plus {dial_zero_during_total} more times during a rotation. So, in this example, the new password would be {dial_zero_at_end + dial_zero_during_total}.")


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
