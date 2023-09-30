def find_best_subarray(nums, k):
    n = len(nums)
    if n < k:
        return -1
    
    current_sum = sum(nums[0:k])
    largest_sum = current_sum
    left = 0
    right = k - 1

    while right < n - 1:
        right += 1
        current_sum += nums[right]
        current_sum -= nums[left]
        left += 1
        largest_sum = max(largest_sum, current_sum)

    return largest_sum