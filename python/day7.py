def count_overbag(rules, color):
    overbags = set()
    for key, values in rules.items():
        for value in values:
            if color in value:
                overbags.add(key)
                overbags.update(count_overbag(rules, key))
    return overbags


def count_innerbags(rules, color):
    count = 0
    values = rules[color]
    for num, col in values:
        if num == 'no':
            return count
        else:
            count += int(num)
            count += int(num) * count_innerbags(rules, col)
    return count   


if __name__ == "__main__":
    with open('../inputs/day7.txt') as f:
        lines = f.readlines()
    
    bag_rules = {}
    for line in lines:
        head, tail = line.split(" bags contain ")
        num_list = [t.split(' ')[0] for t in tail.split(", ")]
        color_list = [" ".join(t.split(' ')[1:3]) for t in tail.split(", ")]
        tail_list = list(zip(num_list, color_list))
        bag_rules[head] = tail_list
    # print(list(bag_rules.items())[:10])

    # Task 1
    bag_set = count_overbag(bag_rules, 'shiny gold')
    print(len(bag_set))

    # Task 2
    bag_count = count_innerbags(bag_rules, 'shiny gold')
    print(bag_count)
    