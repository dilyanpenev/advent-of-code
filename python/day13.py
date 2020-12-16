import sys
from math import gcd

def find_time_left(timestamp, bus_id):
    return bus_id - timestamp % bus_id


if __name__ == "__main__":
    with open('../inputs/day13.txt') as f:
        lines = f.readlines()
    timestamp = int(lines[0])
    ids = lines[1].split('\n')[0].split(',')

    # Task 1
    busses = [int(bus) for bus in ids if bus != 'x']

    dict = {}
    for bus in busses:
        dict[bus] = find_time_left(timestamp, bus)

    soon = min(dict.values())
    for key, value in dict.items():
        if value == soon:
            print(key*value)
            break

    # Task 2
    x_count = 0
    schedule = {}
    for id in ids:
        if id == 'x':
            x_count += 1
        else:
            schedule[int(id)] = x_count
            x_count += 1

    result = 100000000000000
    step_size = 1
    found_busses = set()
    while True:
        result += step_size
        for bus, time in schedule.items():
            if (result+time) % bus != 0:
                break
            elif bus not in found_busses:
                found_busses.add(bus)
                step_size = (bus * step_size) // gcd(bus, step_size)
        else:
            print(result)
            sys.exit()
        