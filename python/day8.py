def execute_instr(instr):
    global accumulator
    if instr[0] == 'acc':
        accumulator += int(instr[1])
        return 1
    elif instr[0] == 'jmp':
        return int(instr[1])
    else:
        return 1


def duplicate_instr(instr):
    copy = []
    for line in instr:
        copy.append(line)
    return copy


def check_if_terminates(instr_set, length):
    global accumulator
    instr_pointer = 0
    visited_instr = []

    while True:
        if instr_pointer >= length:
            return True
        if instr_pointer in visited_instr:
            return False
        visited_instr.append(instr_pointer)
        instr_pointer += execute_instr(instr_set[instr_pointer])

if __name__ == "__main__":
    with open('../inputs/day8.txt') as f:
        lines = f.readlines()

    instr = []
    for line in lines:
        instr.append((line.replace('\n', '').split(' ')))

    # TASK 1
    accumulator = 0
    length = len(instr)
    check_if_terminates(instr, length)
    print(accumulator)

    # TASK 2
    for i in range(length):
        copy_instr = instr.copy()
        accumulator = 0
        if instr[i][0] == 'jmp':
            copy_instr[i][0] = 'nop'
        elif instr[i][0] == 'nop':
            copy_instr[i][0] = 'jmp'
        else:
            continue
        if check_if_terminates(copy_instr, length):
            break
        if copy_instr[i][0] == 'jmp':
            copy_instr[i][0] = 'nop'
        elif copy_instr[i][0] == 'nop':
            copy_instr[i][0] = 'jmp'
    print(accumulator)
