# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        values = []
        def dfs(node):
            if not node:
                return True
            dfs(node.left)
            values.append(node.val)
            dfs(node.right)
        dfs(root)
        for i in range(len(values) - 1):
            if values[i] >= values[i + 1]:
                return False
        return True
