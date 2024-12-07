class Solution:
    def minReorder(self, n: int, connections: List[List[int]]) -> int:
        seen = set()
        adj_list = {i: set() for i in range(n)}
        adj_list_reversed = {j: set() for j in range(n)}
        for i, j in connections:
            adj_list[i].add(j)
            adj_list_reversed[j].add(i)

        def dfs(node, adj_list, adj_list_reversed, seen):
            num_wrong_direction = 0
            for dest in adj_list[node]:
                if dest not in seen:
                    num_wrong_direction += 1
                    num_wrong_direction += dfs(dest, adj_list, adj_list_reversed, seen)
            seen.add(node)
            for src in adj_list_reversed[node]:
                num_wrong_direction += dfs(src, adj_list, adj_list_reversed, seen)
            return num_wrong_direction

        return dfs(0, adj_list, adj_list_reversed, seen)
