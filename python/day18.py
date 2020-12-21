def is_number(char):
    try:
        int(char)
        return True
    except ValueError:
        return False


def calculate(problem):
    result = 0
    skip = 0
    operator = '+'
    elements = list(problem)
    for idx, element in enumerate(elements):
        if skip > 0:
            skip -= 1
            continue
        if is_number(element):
            if operator == '+':
                result += int(element)
            else:
                result *= int(element)
        elif element == '+' or element == '*':
            operator = element
        elif element == '(':
            if operator == '+':
                a, b = calculate(problem[idx+1:])
                result += a
            else:
                a, b = calculate(problem[idx+1:])
                result *= a
            skip = b+1
        elif element == ')':
            return result, idx
    return result


def puzzle1(problems):
    total = 0
    for problem in problems:
        total += calculate(problem)
    return total


if __name__ == "__main__":
    with open('../inputs/day18.txt') as f:
        problems = [line.strip().replace(' ', '') for line in f.readlines()] 

    print(puzzle1(problems))
    # print(calculate('((2+4*9)*(6+9*8+6)+6)+2+4*2'))