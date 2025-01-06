class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        seen = set()
        graph = {i: set() for i in range(n)}
        for edge in edges:
            graph[edge[0]].add(edge[1])
            graph[edge[1]].add(edge[0])

        stack = [source]

        if source == destination:
            return True

        while stack:
            curr = stack.pop()
            if curr not in seen:
                seen.add(curr)
                for neighbor in graph[curr]:
                    if neighbor not in seen:
                        if neighbor == destination:
                            return True
                        stack.append(neighbor)
        
        return False
