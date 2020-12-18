def encode_value(num, mask):
    binary = '{0:036b}'.format(num)
    bin_list = list(binary)
    for idx, char in enumerate(mask):
        if char == '0':
            bin_list[idx] = '0'
        elif char == '1':
            bin_list[idx] = '1'
    binary = "".join(bin_list)
    return int(binary, 2)


def encode_address(num, mask):
    binary = '{0:036b}'.format(num)
    bin_list = list(binary)
    all_addresses = [bin_list]
    for idx, char in enumerate(mask):
        to_add = []
        for lst in all_addresses:
            if char == '1':
                lst[idx] = '1'
            elif char == 'X':
                lst[idx] = '0'
                dup = lst.copy()
                dup[idx] = '1'
                to_add.append(dup)
        all_addresses += to_add
    masks = []
    for lst in all_addresses:
        element = int("".join(lst), 2)
        masks.append(element)
    return masks


def puzzle1(lines):
    memory = {}
    mask = ''
    for line in lines:
        if line[1] == 'a':
            mask = line.replace('mask = ', '')
        else:
            index, value = line.split('] = ')
            index = int(index.replace('mem[', ''))
            value = int(value)
            memory[index] = encode_value(value, mask)
    summ = 0
    for v in memory.values():
        summ += v
    return summ


def puzzle2(lines):
    memory = {}
    mask = ''
    for line in lines:
        if line[1] == 'a':
            mask = line.replace('mask = ', '')
        else:
            index, value = line.split('] = ')
            index = int(index.replace('mem[', ''))
            value = int(value)
            addresses = encode_address(index, mask)
            for address in addresses:
                memory[address] = value
    summ = 0
    for v in memory.values():
        summ += v
    return summ


if __name__ == "__main__":
    with open('../inputs/day14.txt') as f:
        lines = [line.strip() for line in f.readlines()]

    print(puzzle1(lines))

    print(puzzle2(lines))
    