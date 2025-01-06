class Solution:
    def reachableNodes(self, n: int, edges: List[List[int]], restricted: List[int]) -> int:
        from collections import defaultdict

        graph = defaultdict(list)
        for edge in edges:
            graph[edge[0]].append(edge[1])
            graph[edge[1]].append(edge[0])

        restricted_or_seen = set(restricted)
            
        def dfs(node):
            total = 1
            restricted_or_seen.add(node)
            for child in graph[node]:
                if child not in restricted_or_seen:
                    restricted_or_seen.add(child)
                    total += dfs(child)
            return total
            
        return dfs(0)
