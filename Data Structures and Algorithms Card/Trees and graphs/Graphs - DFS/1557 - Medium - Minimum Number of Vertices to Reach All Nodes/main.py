class Solution:
    def findSmallestSetOfVertices(self, n: int, edges: List[List[int]]) -> List[int]:
        destinations = {edge[1] for edge in edges}
        answer = []
        for i in range(n):
            if i not in destinations:
                answer.append(i)
        return answer

        """
        original_edges = {tuple(edge) for edge in edges}

        undirected_graph = {i: set() for i in range(n)}
        for edge in edges:
            undirected_graph[edge[0]].add(edge[1])
            undirected_graph[edge[1]].add(edge[0])

        seen = set()
        answer = []

        def dfs(node):
            all_outgoing = True
            if node not in seen:
                seen.add(node)
                for neighbor in undirected_graph[node]:
                    if (neighbor, node) in original_edges:
                        all_outgoing = False
                        break
                    
                if all_outgoing:
                    answer.append(node)

                for neighbor in undirected_graph[node]:
                    if neighbor not in seen:
                        dfs(neighbor)

        dfs(0)
        return answer
        """
