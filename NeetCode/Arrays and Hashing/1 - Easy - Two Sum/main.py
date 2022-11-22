class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        indices = {}
        for i in range(len(nums)):
            searching_for = target - nums[i]
            if searching_for in indices:
                return [indices[searching_for], i]
            indices[nums[i]] = i        
        """
        indices = {}
        for i in range(len(nums)):
            if indices.get(nums[i]):
                indices[nums[i]] += [i]
            else:
                indices[nums[i]] = [i]
                
        for i in range(len(nums)):
            searching_for = target - nums[i]
            index = indices.get(searching_for)
            if index:
                if i == index[0]:
                    if len(index) == 2:
                        return [i, index[1]]
                    else:
                        continue
                else:
                    return [i, index[0]]
        """
