class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        from collections import deque

        m = len(mat)
        n = len(mat[0])

        offset = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        answer = [[None] * n for _ in range(m)]
        queue = deque()

        seen = set()
        which_zero = 0
        for i in range(m):
            for j in range(n):
                if mat[i][j] == 0:
                    answer[i][j] = 0
                    which_zero += 1
                    queue.append(((i, j), which_zero))
                    seen.add((i, j))
        val = 0
        num_zeros = len(queue)
        last_zero = -1
        while queue:
            (x_cor, y_cor), this_zero = queue.popleft()
            if last_zero > this_zero:
                val += 1
            for dx, dy in offset:
                new_x, new_y = x_cor + dx, y_cor + dy
                if not (0 <= new_x < m) or not (0 <= new_y < n):
                    continue
                if mat[new_x][new_y] == 1 and (new_x, new_y) not in seen:
                        answer[new_x][new_y] = val + 1
                        seen.add((new_x, new_y))
                        queue.append(((new_x, new_y), this_zero))
            last_zero = this_zero
            if num_zeros == 1:
                val += 1

        return answer
