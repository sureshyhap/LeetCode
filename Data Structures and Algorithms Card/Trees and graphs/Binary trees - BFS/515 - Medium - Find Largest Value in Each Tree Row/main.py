# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def largestValues(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
        from collections import deque
        queue = deque([root])
        answer = []
        while queue:
            level_size = len(queue)
            maximum = float("-inf")
            for _ in range(level_size):
                node = queue.popleft()
                if node.val > maximum:
                    maximum = node.val
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            answer.append(maximum)
        return answer
