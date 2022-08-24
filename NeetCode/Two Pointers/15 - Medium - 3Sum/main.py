class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        semi_unique = {num : 0 for num in nums}
        for num in nums:
            semi_unique[num] += 1
        nums = []
        for number, frequency in semi_unique.items():
            freq = 3 if frequency > 2 else frequency
            for _ in range(freq):
                nums.append(number)
        nums.sort()
        results = []
        bound = len(nums) - 1
        i = 0
        for num1 in nums[:-2]:
            j = bound
            for num2 in nums[:i+1:-1]:
                if num1 > 0 and num2 > 0:
                    return results
                if num1 < 0 and num2 < 0:
                    if nums[-1] < 0:
                        return results
                    else:
                        break
                if num1 == 0 and num2 == 0:
                    results.append([0, 0, 0])
                    return results
                number_to_search = -(num1 + num2)
                found = self.binary_search(nums, number_to_search, i + 1, j - 1)
                if found:
                    result = [num1, number_to_search, num2]
                    found_in_results = self.binary_search(results, result, 0, len(results) - 1)
                    if not found_in_results:
                        results.append(result)
                j -= 1
            i += 1
        return results
    
    def binary_search(self, sequence, value, start: int, end: int) -> bool:
        i = (start + end) // 2
        if start > end:
            return False
        if start == end and sequence[i] != value:
            return False
        if sequence[i] < value:
            return self.binary_search(sequence, value, i + 1, end)
        if sequence[i] > value:
            return self.binary_search(sequence, value, start, i - 1)
        return True
