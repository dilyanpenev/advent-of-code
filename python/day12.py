directions = {'E':(1, 0), 'N':(0, 1), 'W':(-1, 0), 'S':(0, -1)}
left_turn = {'E':'N', 'N':'W', 'W':'S', 'S':'E'}
right_turn = {'E':'S', 'N':'E', 'W':'N', 'S':'W'}

def move_ship(amount, x, y, value_x, value_y):
    x += value_x * amount
    y += value_y * amount
    return x, y


def puzzle1(lines):
    facing = 'E'
    x = 0
    y = 0
    for line in lines:
        instr = line[0]
        value = int(line[1:])
        if instr in directions.keys():
            value_x, value_y = directions[instr]
            x, y = move_ship(value, x, y, value_x, value_y)
        else:
            if instr == 'L':
                while value>0:
                    facing = left_turn[facing]
                    value -= 90
            elif instr == 'R':
                while value>0:
                    facing = right_turn[facing]
                    value -= 90
            else:
                value_x, value_y = directions[facing]
                x, y = move_ship(value, x, y, value_x, value_y)
    return abs(x) + abs(y)

def puzzle2(lines):
    x, y = 0, 0
    waypoint_x, waypoint_y = 10, 1
    for line in lines:
        instr = line[0]
        value = int(line[1:])
        if instr in directions.keys():
            value_x, value_y = directions[instr]
            waypoint_x, waypoint_y = move_ship(value, waypoint_x, waypoint_y, value_x, value_y)
        else:
            if instr == 'L':
                while value>0:
                    temp = waypoint_y
                    waypoint_y = waypoint_x
                    waypoint_x = -temp
                    value -= 90
            elif instr == 'R':
                while value>0:
                    temp = waypoint_x
                    waypoint_x = waypoint_y
                    waypoint_y = -temp
                    value -= 90
            else:
                x, y = move_ship(value, x, y, waypoint_x, waypoint_y)
    return abs(x) + abs(y)


if __name__ == "__main__":
    with open('../inputs/day12.txt') as f:
        lines = [line.strip() for line in f.readlines()]

    print(puzzle1(lines))

    print(puzzle2(lines)) 
        