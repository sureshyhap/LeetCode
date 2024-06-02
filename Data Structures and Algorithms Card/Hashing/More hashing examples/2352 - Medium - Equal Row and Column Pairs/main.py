class Solution:
    def equalPairs(self, grid: List[List[int]]) -> int:
        n = len(grid)
        rows = {}
        cols = {}
        for i in range(n):
            row = tuple(grid[i])
            if row in rows:
                rows[row] += 1
            else:
                rows[row] = 1
            col = tuple([r[i] for r in grid])
            if col in cols:
                cols[col] += 1
            else:
                cols[col] = 1
        result = 0
        for row, count in rows.items():
            result += (count * cols.get(row, 0))
        return result
