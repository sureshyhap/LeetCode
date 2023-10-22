def answer_queries(nums, queries, limit):
    n = len(nums)
    prefix_sum = [0] * n
    prefix_sum[0] = nums[0]
    
    for i in range(1, n):
        prefix_sum[i] = prefix_sum[i - 1] + nums[i]

    boolean_results = []

    for i, query in enumerate(queries):
        result = prefix_sum[query[1]] - prefix_sum[query[0]] + nums[query[0]]
        boolean_results.append(result < limit)

    return boolean_results
