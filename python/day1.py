import sys

def bin_search(array, q):
    if len(array)<1:
        return False
    mid = len(array)//2
    if array[mid] == q:
        return True
    elif q < array[mid]:
        return bin_search(array[:mid], q)
    else:
        return bin_search(array[mid+1:], q)

if __name__ == "__main__":
    with open('../inputs/day1.txt') as f:
        nums = []
        for line in f:
            line = line.split()
            if line:            
                nums.append(int(line[0]))

    nums.sort()

    # Task 1
    for num in nums:
        q = 2020 - num
        if q < nums[0]:
            continue
        if bin_search(nums, q):
            print(num*q)
            break

    # Task 2
    for num1 in nums:
        for num2 in nums:
            q = 2020 - num1 - num2
            if num1 == num2 | q < nums[0]:
                continue
            if bin_search(nums, q):
                print(num1*num2*q)
                sys.exit()
