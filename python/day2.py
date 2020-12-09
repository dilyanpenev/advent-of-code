def check_occurrences(str, letter, min_chars, max_chars):
    count = 0
    for char in str:
        if char == letter:
            count += 1
    if count >= min_chars:
        if count <= max_chars:
            return True
    else:
        return False


def check_positions(str, letter, pos1, pos2):
    if len(str) < pos2:
        return False
    pos1 = pos1 - 1
    pos2 = pos2 - 1
    if str[pos1] == letter:
        if str[pos2] == letter:
            return False
        else:
            return True
    else:
        if str[pos2] == letter:
            return True
        else:
            return False


if __name__ == "__main__":
    with open('../inputs/day2.txt') as f:
        lines = []
        for line in f:
            line = line.split()
            if line:            
                lines.append(line)

    minRange = [int(i[0].split('-')[0]) for i in lines]
    maxRange = [int(i[0].split('-')[1]) for i in lines]
    letters = [i[1][0] for i in lines]
    passwords = [i[2] for i in lines]

    # Task 1
    correct_passwords = 0
    for k in range(len(lines)):
        if (check_occurrences(passwords[k], letters[k], minRange[k], maxRange[k])):
            correct_passwords += 1

    print(correct_passwords)

    # Task 2
    valid_passwords = 0
    for n in range(len(lines)):
        if (check_positions(passwords[n], letters[n], minRange[n], maxRange[n])):
            valid_passwords += 1

    print(valid_passwords)
