"""
class Solution:
    def maxDistance(self, colors: List[int]) -> int:
        left = 0
        right = len(colors) - 1
        distances = [[0] * len(colors) for _ in range(len(colors))]
        def dist(colors, left, right):
            if colors[left] != colors[right]:
                return right - left
            else:
                if distances[left][right] > 0:
                    return distances[left][right]
                elif distances[right][left] > 0:
                    return distances[right][left]
                result1 = dist(colors, left + 1, right)
                distances[left + 1][right] = result1
                result2 = dist(colors, left, right - 1)
                distances[left][right - 1] = result2
                return max(result1, result2)
        return dist(colors, left, right)
"""

class Solution:
    def maxDistance(self, colors: List[int]) -> int:
        distances = [[None] * len(colors) for _ in range(len(colors))]
        for i in range(len(colors)):
            distances[i][i] = 0
        for offset in range(1, len(colors)):
            for i in range(len(colors) - offset):
                j = i + offset
                if colors[i] != colors[j]:
                    distances[i][j] = offset
                else:
                    distances[i][j] = max(distances[i + 1][j], distances[i][j - 1])
        return distances[0][len(colors) - 1]
