class Solution:
    def sumOfUnique(self, nums: List[int]) -> int:
        counts = {}
        for num in nums:
            if num in counts:
                counts[num] += 1
            else:
                counts[num] = 1
        result = 0
        for num, count in counts.items():
            if count == 1:
                result += num
        return result
