def find_length(s: str) -> int:
    n = len(s)
    zero_at_index = None
    left = right = 0
    longest = 0

    while right < n:
        if s[right] == "1":
            right += 1
        else:
            if not zero_at_index:
                zero_at_index = right
            else:
                left = zero_at_index + 1
                zero_at_index = right
            right += 1
        longest = max(longest, right - left)

    return longest

print(find_length("1101100111"))
