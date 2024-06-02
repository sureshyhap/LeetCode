class Solution:
    def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:
        prefix_sum = [0]
        counts = {0: 1}
        answer = 0
        for num in nums:
            prefix_sum.append(num + prefix_sum[-1])
            answer += counts.get(prefix_sum[-1] - goal, 0)
            if prefix_sum[-1] in counts:
                counts[prefix_sum[-1]] += 1
            else:
                counts[prefix_sum[-1]] = 1
        return answer
