from collections import deque
class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        if grid[0][0] == 1:
            return -1

        n = len(grid)
        
        queue = deque([(0, 0, 1)])
        seen = {(0, 0)}
        directions = [(0, 1), (1, 1), (1, 0), (1, -1), (0, -1), (-1, -1), (-1, 0), (-1, 1)]
        while queue:
            node = queue.popleft()
            i, j, length = node
            if i == n - 1 and j == n - 1:
                return length
            for x, y in directions:
                new_row, new_col = i + x, j + y
                if 0 <= new_row < n and 0 <= new_col < n:
                    if grid[new_row][new_col] == 0:
                        if (new_row, new_col) not in seen:
                            seen.add((new_row, new_col))
                            queue.append((new_row, new_col, length + 1))

        return -1
