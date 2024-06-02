import heapq

class Solution:
    def largestUniqueNumber(self, nums: List[int]) -> int:
        """
        counts = {}
        n = len(nums)
        for i, value in enumerate(nums):
            if value not in counts:
                counts[value] = 1
            else:
                counts[value] += 1
        result = -1
        print(counts)
        for i, j in counts.items():
            if j == 1:
                result = max(result, i)
        return result
        """

        """
        if len(nums) == 1:
            return nums[0]
        nums.sort()
        counts = 0
        i = len(nums) - 1
        while i >= 0:
            while nums[i] == nums[i - 1]:
                i -= 1
                counts += 1
            if counts == 0:
                return nums[i]
            else:
                i -= 1
                counts = 0
        return -1
        """
        if len(nums) == 1:
            return nums[0]
        nums = [-elem for elem in nums]
        heapq.heapify(nums)

        max = heapq.heappop(nums)
        max2 = heapq.heappop(nums)

        if max != max2:
            return -max

        count = 0
        while len(nums) > 0:
            while max == max2:
                max = max2
                max2 = heapq.heappop(nums)
                count += 1
            if count == 0:
                return -max
            else:
                count = 0
                if len(nums) == 0:
                    return -max2
                max = max2
                max2 = heapq.heappop(nums)
        return -1
