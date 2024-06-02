class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        jewel_types = set(jewels)
        num_jewels = 0
        for stone in stones:
            if stone in jewel_types:
                num_jewels += 1
        return num_jewels
