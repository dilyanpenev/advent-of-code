def puzzle1(adaptors):
    current = 0
    diffs = {1: 0, 2: 0, 3: 1}
    while True:
        for i in range(1, 4):
            current += 1
            if current in adaptors:
                diffs[i] += 1
                break
        else:
            return diffs[1] * diffs[3]


def puzzle2(adaptors):
    adaptors.sort()
    device = adaptors[-1] + 3
    adaptors.append(device)
    count = {0: 1}
    for element in adaptors:
        count[element] = 0
        for i in range(1, 4):
            if element - i in count.keys():
                count[element] += count[element-i]
    return list(count.values())[-1]


if __name__ == "__main__":
    with open('../inputs/day10.txt') as f:
        lines = f.readlines()
        adaptors = [int(line.strip()) for line in lines]

    print(puzzle1(adaptors))

    print(puzzle2(adaptors))