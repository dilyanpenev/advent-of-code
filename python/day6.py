def count_distinct_chars(str_list):
    txt = "".join(str_list)
    chars = list(set([char for char in txt]))
    return len(chars)


def count_all_answered(str_list):
    chars = [char for char in str_list[0]]
    result = 0
    for ch in chars:
        for seq in str_list:
            if ch not in seq:
                break
        else:
            result += 1
    return result


if __name__ == "__main__":
    with open('../inputs/day6.txt') as f:
        lines = f.readlines()
    answers = []
    buffer = []
    for line in lines:
        if line == "\n":
            answers.append(buffer)
            buffer = []
        else:
            buffer += line.split()
    if buffer:
        answers.append(buffer)
    
    sum = 0
    sum_all = 0
    for ans in answers:
        sum += count_distinct_chars(ans)
        sum_all += count_all_answered(ans)

    print(sum)
    print(sum_all)
