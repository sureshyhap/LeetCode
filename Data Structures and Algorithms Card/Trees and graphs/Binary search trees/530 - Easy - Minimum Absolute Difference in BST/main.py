# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getMinimumDifference(self, root: Optional[TreeNode]) -> int:
        min_diff = float("inf")
        def dfs(node):
            if not node:
                return None, None
            largest_left, smallest_left = dfs(node.left)
            largest_right, smallest_right = dfs(node.right)
            nonlocal min_diff
            if largest_left != None:
                min_diff = min(min_diff, node.val - largest_left)
            if smallest_right != None:
                min_diff = min(min_diff, smallest_right - node.val)
            
            if node.left == None and node.right == None:
                return node.val, node.val
            elif node.left and node.right:
                return largest_right, smallest_left
            elif node.left:
                return node.val, smallest_left
            elif node.right:
                return largest_right, node.val
        dfs(root)
        return min_diff
