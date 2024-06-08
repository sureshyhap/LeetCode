class Solution:
    def customSortString(self, order: str, s: str) -> str:
        relative_indices = {}
        i = 0
        for c in order:
            relative_indices[c] = i
            i += 1
        s_list_sorted = sorted(list(s), key=lambda c: relative_indices.get(c, float("inf")))
        return "".join(s_list_sorted)
