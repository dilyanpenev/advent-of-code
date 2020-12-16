def check_sum(arr, num):
    for element in arr:
        to_find = num - element
        if to_find in arr and to_find != element:
            break
    else:
        return False
    return True


def puzzle2(nums, goal):
    for index, num in enumerate(nums):
        sums = 0
        min_num = num
        max_num = num
        pointer = index
        while sums < goal:
            current = nums[pointer]
            sums += current
            if current < min_num:
                min_num = current
            if current > max_num:
                max_num = current
            if sums == goal:
                return min_num + max_num
            pointer += 1
    return None


if __name__ == "__main__":
    with open('../inputs/day9.txt') as f:
        lines = f.readlines()
        nums = [int(line.strip()) for line in lines]
    
    base = nums[:25]
    for i in range(25, len(nums)):
        current = nums[i]
        if not check_sum(base, current):
            break
        base.pop(0)
        base.append(current)
    print(current)

    print(puzzle2(nums, current))