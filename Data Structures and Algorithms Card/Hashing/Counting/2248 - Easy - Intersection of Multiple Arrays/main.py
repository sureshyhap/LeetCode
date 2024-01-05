class Solution:
    def intersection(self, nums: List[List[int]]) -> List[int]:
        result = set(nums[0])
        m = len(nums)
        for i in range(1, m):
            present_row = set(nums[i])
            result = result.intersection(present_row)
        result_list = list(result)
        return sorted(result_list)
