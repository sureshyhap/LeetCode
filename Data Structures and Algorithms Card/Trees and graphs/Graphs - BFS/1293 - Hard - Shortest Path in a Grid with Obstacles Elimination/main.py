class Solution:
    def shortestPath(self, grid: List[List[int]], k: int) -> int:
        from collections import deque

        def is_valid(i, j):
            return (0 <= i < m) and (0 <= j < n)

        m = len(grid)
        n = len(grid[0])
        if m == 1 and n == 1:
            return 0
        after_elimination = [row[:] for row in grid]
        queue = deque([(0, 0, k, 0)])
        offset = ((0, 1), (1, 0), (0, -1), (-1, 0))
        seen_table = {}

        while queue:
            i, j, remaining, steps_taken = queue.popleft()
            for delta_row, delta_col in offset:
                new_i, new_j = i + delta_row, j + delta_col
                if is_valid(new_i, new_j):
                    if after_elimination[new_i][new_j] == 0:
                        if (new_i, new_j) not in seen_table:
                            seen_table[(new_i, new_j)] = deque([(remaining, steps_taken + 1)])
                            queue.append((new_i, new_j, remaining, steps_taken + 1))
                        else:
                            present_k, present_num_steps = seen_table[(new_i, new_j)][-1]
                            if grid[new_i][new_j] == 0:
                                if remaining > present_k:
                                    seen_table[(new_i, new_j)].append((remaining, steps_taken + 1))
                                    queue.append((new_i, new_j, remaining, steps_taken + 1))
                    else:
                        if remaining > 0:
                            after_elimination[new_i][new_j] = 0
                            seen_table[(new_i, new_j)] = deque([(remaining - 1, steps_taken + 1)])
                            queue.append((new_i, new_j, remaining - 1, steps_taken + 1))
                        else:
                            if len(seen_table[(i, j)]) > 1:
                                seen_table[(i, j)].popleft()
                                rem, steps = seen_table[(i, j)][0]
                                queue.appendleft((i, j, rem, steps))
                                break
            if (m - 1, n - 1) in seen_table:
                return seen_table[(m - 1, n - 1)][0][1]
        return -1
