class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        s_index_map = {}
        for i, c in enumerate(s):
            if not s_index_map.get(c):
                s_index_map[c] = [i]
            else:
                s_index_map[c].append(i)
        t_index_map = {}
        for i, c in enumerate(t):
            if not t_index_map.get(c):
                t_index_map[c] = [i]
            else:
                t_index_map[c].append(i)
        return list(s_index_map.values()) == list(t_index_map.values())
