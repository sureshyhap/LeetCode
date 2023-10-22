class Solution:
    def waysToSplitArray(self, nums: List[int]) -> int:
        n = len(nums)
        sum_left = nums[0]
        sum_right = sum(nums[1:])
        answer = 1 if sum_left >= sum_right else 0

        for i in range(1, n - 1):
            sum_left += nums[i]
            sum_right -= nums[i]
            if sum_left >= sum_right:
                answer += 1
            
        return answer
