def decode_row(sequence):
    min_row = 0
    max_row = 127
    for char in sequence:
        if char == 'F':
            max_row = (max_row + min_row) // 2
        else:
            min_row = (max_row + min_row) // 2 + 1
    return min_row


def decode_column(sequence):
    min_row = 0
    max_row = 7
    for char in sequence:
        if char == 'L':
            max_row = (max_row + min_row) // 2
        else:
            min_row = (max_row + min_row) // 2 + 1
    return min_row


def calculate_seat(sequence):
    row = decode_row(sequence[:7])
    col = decode_column(sequence[7:])
    return row * 8 + col


if __name__ == "__main__":
    with open('../inputs/day5.txt') as f:
        lines = f.readlines()
        lines = [line[:10] for line in lines]

    max_seat = 0
    seat_map = [i for i in range(0, 894)]
    for line in lines:
        val = calculate_seat(line)
        if val > max_seat:
            max_seat = val
        if val in seat_map:
            seat_map.remove(val)
    print(max_seat)
    print(seat_map)
    