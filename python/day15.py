def puzzle(nums, index):
    freq_dict = {num: idx + 1 for idx, num in enumerate(nums[:-1])}
    last = nums[-1]
    for i in range(len(nums), index):
        if last in freq_dict.keys():
            next_elem = i - freq_dict[last]
        else:
            next_elem = 0
        freq_dict[last] = i
        last = next_elem
    return last


if __name__ == "__main__":
    start_nums = [16,11,15,0,1,7]

    print(puzzle(start_nums, 2020))
    print(puzzle(start_nums, 30000000))
