class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        power_set = []
        num_subsets = 2 ** len(nums)
        for binary_count in range(num_subsets):
            binary_list = []
            binary_num = binary_count
            for _ in range(len(nums)):
                binary_list.append(binary_num % 2)
                binary_num >>= 1
            nums_filtered = []
            for i in range(len(nums)):
                if nums[i] != 0 or binary_list[i] == 0:
                    nums_filtered.append(nums[i] * binary_list[i])
                else:
                    # 11 is arbitrarily chosen to be outside of the
                    # range of possible numbers
                    nums_filtered.append(11)
            nums_filtered = list(filter(lambda x : x != 0, nums_filtered))
            nums_filtered = list(map(lambda x: 0 if x == 11 else x, nums_filtered))
            power_set.append(nums_filtered)
        return power_set
