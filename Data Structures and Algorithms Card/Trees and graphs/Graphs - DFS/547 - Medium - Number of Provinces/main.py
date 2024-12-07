class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        num_comp = 0
        seen = set()
        def dfs(node, seen):
            seen.add(node)
            for j in range(len(isConnected)):
                if isConnected[node][j] == 1 and j not in seen:
                    seen.add(j)
                    dfs(j, seen)
            return 1
        for i in range(len(isConnected)):
            if i not in seen:
                num_comp += dfs(i, seen)
        return num_comp

        """
        n = len(isConnected)
        num_comp_count = n
        connectivity = {i: set([i]) for i in range(n)}
        for i in range(n):
            for j in range(i, n):
                if isConnected[i][j] == 1:
                    if connectivity[i] & connectivity[j] == set():
                        num_comp_count -= 1
                    new_comp = connectivity[i] | connectivity[j]
                    for k in new_comp:
                        connectivity[k] = new_comp
        return num_comp_count
        """
