class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        graph = {i: set() for i in range(n)}
        for edge in edges:
            graph[edge[0]].add(edge[1])
            graph[edge[1]].add(edge[0])
        seen = set()

        def dfs(node):
            if node not in seen:
                seen.add(node)
                for neighbor in graph[node]:
                    dfs(neighbor)
                return 1
            return 0

        total = 0
        for i in range(n):
            total += dfs(i)
        return total
