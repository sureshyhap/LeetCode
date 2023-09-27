def longest_subarray(nums, k) -> int:
    n = len(nums)
    left, right = 0, 0
    best_length = 0
    current_sum = nums[left]
    length = 0

    while nums[left] > k:
        left += 1
        right += 1
    
    while right < n - 1:
        if current_sum <= k:
            length += 1
            right += 1
            current_sum += nums[right]
            best_length = max(best_length, length)
        else:
            current_sum -= nums[left]
            left += 1
            length -= 1
            length = max(length, 0)
            
    return best_length

nums = [3, 2, 1, 3, 1, 1]
print(longest_subarray(nums, 5))
nums2 = [3, 1, 2, 7, 4, 2, 1, 1, 5]
print(longest_subarray(nums2, 8))
