class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        n = len(nums)
        original_as_hash_table = {nums[i] : i for i in range(n)}
        for i in range(n):
            difference = target - nums[i]
            if difference in original_as_hash_table:
                first, second = i, original_as_hash_table[difference]
                if first != second:
                    return first, second