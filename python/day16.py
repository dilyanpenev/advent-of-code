import re
from collections import defaultdict

def load_input():
    rules = []
    tickets = []
    with open('../inputs/day16.txt') as f:
        line = f.readline()
        while line != '\n':
            rules.append(line.strip())
            line = f.readline()

        _ = f.readline()
        my_ticket = f.readline().strip()
        
        _ = f.readline()
        _ = f.readline()
        line = f.readline()
        while line != '':
            tickets.append(line.strip())
            line = f.readline()
    return rules, my_ticket, tickets


def extract_rules(rules):
    valids = {}
    for rule in rules:
        lst = []
        key, values = rule.split(': ')
        left, right = values.split(' or ')
        left = [int(num) for num in left.split('-')]
        right = [int(num) for num in right.split('-')]
        for i in range(left[0], left[1]+1):
            lst.append(i)
        for i in range(right[0], right[1]+1):
            lst.append(i)
        valids[key] = lst
    return valids


def check_values(rules, values):
    summ = 0
    to_remove = set()
    for idx, row in enumerate(values):
        value = [int(i) for i in row.split(',')]
        for num in value:
            for rule in rules.values():
                if num in rule:
                    break
            else:
                summ += num
                to_remove.add(idx)
    to_remove = list(to_remove)
    new = []
    for idx, value in enumerate(values):
        if idx not in to_remove:
            new.append(value)
    return summ, new


def match_fields(dct, values):
    field_map = defaultdict(list)
    tickets = []
    for row in values:
        value = [int(i) for i in row.split(',')]
        tickets.append(value)
    for i in range(len(tickets[0])):
        for key, ranges in dct.items():
            if key in field_map.keys():
                continue
            is_match = False
            for ticket in tickets:
                if ticket[i] not in ranges:
                    break
            else:
                is_match = True
            if is_match:
                field_map[key] += [i]
                break
    return field_map


def puzzle1():
    rules, _, tickets = load_input()
    valid_fields = extract_rules(rules)
    return check_values(valid_fields, tickets)


# def puzzle2(tickets):
#     rules, my_ticket, _ = load_input()
#     my_ticket = [int(i) for i in my_ticket.split(',')]
#     valid_fields = extract_rules(rules)
#     field_map = match_fields(valid_fields, tickets)
#     print(field_map)
#     mult = 1
#     # for key, value in field_map.items():
#     #     if re.search("departure", key):
#     #         mult *= my_ticket[value]
#     return mult



if __name__ == "__main__":
    summ, new_tickets = puzzle1()
    print(summ)

    # print(puzzle2(new_tickets))


