# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        from math import inf
        count = 0
        def dfs(root, max_val):
            nonlocal count
            if not root:
                return
            if max_val > root.val:
                dfs(root.left, max_val)
                dfs(root.right, max_val)
            else:
                count += 1
                dfs(root.left, root.val)
                dfs(root.right, root.val)
        dfs(root, -inf)
        return count
        """
        if not root:
            return 0
        stack = [(root, -float("inf"))]
        result = 0
        while stack:
            node, max_val = stack.pop()
            if node and node.val >= max_val:
                result += 1
                maximum = node.val
            else:
                maximum = max_val
            if node:
                stack.append((node.left, maximum))
                stack.append((node.right, maximum))
        return result
        """
