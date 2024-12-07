class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        m = len(grid)
        n = len(grid[0])
        seen = [[False] * n for _ in range(m)]
        num_islands = 0

        def dfs(i, j, seen):
            if i - 1 >= 0:
                if grid[i - 1][j] == "1" and not seen[i - 1][j]:
                    seen[i - 1][j] = True
                    dfs(i - 1, j, seen)

            if j - 1 >= 0:
                if grid[i][j - 1] == "1" and not seen[i][j - 1]:
                    seen[i][j - 1] = True
                    dfs(i, j - 1, seen)
            
            if i + 1 < m:
                if grid[i + 1][j] == "1" and not seen[i + 1][j]:
                    seen[i + 1][j] = True
                    dfs(i + 1, j, seen)

            if j + 1 < n:
                if grid[i][j + 1] == "1" and not seen[i][j + 1]:
                    seen[i][j + 1] = True
                    dfs(i, j + 1, seen)

        for i in range(m):
            for j in range(n):
                if grid[i][j] == "1" and not seen[i][j]:
                    dfs(i, j, seen)
                    num_islands += 1
        return num_islands
