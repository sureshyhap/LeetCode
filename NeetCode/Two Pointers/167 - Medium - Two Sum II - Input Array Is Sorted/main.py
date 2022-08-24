class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        for i in range(len(numbers)):
            if i > 1 and numbers[i] == numbers[i - 1] and numbers[i] == numbers[i - 2]:
                continue
            if numbers[i] + numbers[-1] < target:
                continue
            else:
                for j in range(len(numbers) - 1, i, -1):
                    if numbers[i] + numbers[j] == target:
                        return [i + 1, j + 1]
                    elif numbers[i] + numbers[j] < target:
                        break
