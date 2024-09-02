class Solution:
    from collections import deque
    import math

    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        queue = deque()
        answer = []
        maximum = -math.inf

        for i in range(0, k):
            if nums[i] >= maximum:
                maximum = nums[i]
                queue.append(maximum)
            while queue and queue[0] < nums[i]:
                queue.popleft()
            if nums[i] < maximum:
                queue.appendleft(nums[i])
        answer.append(maximum)

        for i in range(len(nums) - k):
            if nums[i] == maximum:
                queue.pop()
            if nums[i + k] >= maximum:
                queue.append(nums[i + k])
            while queue and queue[0] < nums[i + k]:
                queue.popleft()
            if nums[i + k] < maximum:
                queue.appendleft(nums[i + k])
            maximum = queue[-1]
            answer.append(maximum)

        return answer
