class Solution:
    def getAverages(self, nums: List[int], k: int) -> List[int]:
        if k == 0:
            return nums
        n = len(nums)
        if n <= 2 * k:
            return [-1] * n
        avgs = [0] * n
        for i in range(k):
            avgs[i] = -1
        for i in range(n - 1, n - k - 1, -1):
            avgs[i] = -1

        summation = sum(nums[:2*k+1])
        avgs[k] = summation
        for i in range(k, n - k - 1):
            summation -= nums[i - k]
            i += 1
            summation += nums[i + k]
            avgs[i] = summation
        for i in range(k, n - k):
            avgs[i] //= (2 * k + 1)
        return avgs
