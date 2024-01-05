def at_most_k_distinct(s: str, k: int) -> int:
    if k == 0:
        return 0
    n = len(s)
    distinct_in_window = 0
    counts = {}
    j = 0
    for i in range(n):
        while distinct_in_window > k:
            counts[s[j]] -= 1
            if counts[s[j]] == 0:
                distinct_in_window -= 1
                del counts[s[j]]
            j += 1
        if s[i] not in counts:
            counts[s[i]] = 1
            distinct_in_window += 1
        else:
            counts[s[i]] += 1
    return distinct_in_window

print(at_most_k_distinct("eceba", 2))

