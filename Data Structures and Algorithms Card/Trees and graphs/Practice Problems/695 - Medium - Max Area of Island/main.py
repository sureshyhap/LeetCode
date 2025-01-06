class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])

        seen = set()

        def dfs(node):
            i = node[0]
            j = node[1]
            area = 0
            if grid[i][j]:
                if (i, j) not in seen:
                    seen.add((i, j))
                    area += 1 
                    if i - 1 >= 0 and grid[i - 1][j]:
                        area += dfs((i - 1, j))
                    if j - 1 >= 0 and grid[i][j - 1]:
                         area += dfs((i, j - 1))
                    if i + 1 < m and grid[i + 1][j]:
                        area += dfs((i + 1, j))
                    if j + 1 < n and grid[i][j + 1]:
                        area += dfs((i, j + 1))
            return area
        
        max_area = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] and (i, j) not in seen:
                    max_area = max(max_area, dfs((i, j)))
        return max_area
        """
        m = len(grid)
        n = len(grid[0])
        vertices = set()
        for i, row in enumerate(grid):
            for j, cell in enumerate(row):
                if cell:
                    vertices.add((i, j))

        graph = {vertex: set() for vertex in vertices}

        for vertex in vertices:
            i = vertex[0]
            j = vertex[1]

            if (i, j + 1) in vertices:
                graph[vertex].add((i, j + 1))
                graph[(i, j + 1)].add(vertex)

            if (i + 1, j) in vertices:
                graph[vertex].add((i + 1, j))
                graph[(i + 1, j)].add(vertex)

        seen = set()

        def dfs(vertex):
            area = 0
            if vertex not in seen:
                area += 1
                seen.add(vertex)
                for neighbor in graph[vertex]:
                    area += dfs(neighbor)
            return area

        max_area = 0
        for vertex in vertices:
            max_area = max(max_area, dfs(vertex))
        return max_area
        """
