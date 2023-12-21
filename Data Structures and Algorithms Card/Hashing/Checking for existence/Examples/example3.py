def main(nums):
    nums_set = set(nums)
    result = []
    for x in nums:
        if ((x + 1) not in nums_set) and ((x - 1) not in nums_set):
            result.append(x)
    return result
