class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        counts = {}
        for num in nums:
            if num in counts:
                counts[num] += 1
            else:
                counts[num] = 1
        answer = 0
        for key, value in counts.items():
            answer += ((value - 1) * value) // 2
        return answer
