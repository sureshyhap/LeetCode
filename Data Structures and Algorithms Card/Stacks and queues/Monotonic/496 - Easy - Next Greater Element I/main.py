        """
        num_to_index = {}
        for i, num in enumerate(nums2):
            num_to_index[num] = i
        result = []
        for num in nums1:
            index = num_to_index[num] + 1
            while index < len(nums2) and num > nums2[index]:
                index += 1
            if index < len(nums2):
                result.append(nums2[index])
            else:
                result.append(-1)
        return result
        """
