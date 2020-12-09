import re

def check_validity(passport, fields):
    passport_str = " ".join(passport)
    for field in fields:
        if field not in passport_str:
            return False
    return True

def check_valid_fields(passport):
    for field in passport:
        if 'byr' in field:
            var = int(field.split(':')[1])
            if var < 1920:
                break
            if var > 2002:
                break
        elif 'iyr' in field:
            var = int(field.split(':')[1])
            if var < 2010:
                break
            if var > 2020:
                break
        elif 'eyr' in field:
            var = int(field.split(':')[1])
            if var < 2020:
                break
            if var > 2030:
                break
        elif 'hcl' in field:
            var = field.split(':')[1]
            if not re.match('^#[0-9a-f]{6}$', var):
                break
        elif 'ecl' in field:
            eye_colors = ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth']
            var = field.split(':')[1]
            if var not in eye_colors:
                break
        elif 'pid' in field:
            var = field.split(':')[1]
            if not re.match('^[0-9]{9}$', var):
                break
        elif 'hgt' in field:
            var = field.split(':')[1]
            if 'cm' in var:
                var = int(var[:-2])
                if var < 150:
                    break
                if var > 193:
                    break
            elif 'in' in var:
                var = int(var[:-2])
                if var < 59:
                    break
                if var > 76:
                    break
            else:
                return False
    else:
        return True
    return False


if __name__ == "__main__":
    # Read passports
    with open('../inputs/day4.txt') as f:
        lines = f.readlines()
    passports = []
    buffer = []
    for line in lines:
        if line == "\n":
            passports.append(buffer)
            buffer = []
        else:
            buffer += line.split()
    if buffer:
        passports.append(buffer)

    required_fields = ['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid']
    count = 0
    for passport in passports:
        if check_validity(passport, required_fields) & check_valid_fields(passport):
                count += 1
    print(count)