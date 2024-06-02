class Solution:
    def findLucky(self, arr: List[int]) -> int:
        freqs = {}
        for num in arr:
            if num in freqs:
                freqs[num] += 1
            else:
                freqs[num] = 1
        max = -1
        for num, count in freqs.items():
            if num == count:
                if num > max:
                    max = num
        return max
