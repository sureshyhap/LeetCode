class Solution:
    def minimumCardPickup(self, cards: List[int]) -> int:
        result = 11e5
        duplicates = {}
        for index, value in enumerate(cards):
            if value in duplicates:
                distance = index - duplicates[value] + 1
                if distance < result:
                    result = distance
            duplicates[value] = index
        return (result if result != 11e5 else -1)
