# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def closestValue(self, root: Optional[TreeNode], target: float) -> int:
        less, more = None, None
        done = None
        def dfs(node):
            nonlocal done
            if node == None or done:
                return
            nonlocal less
            nonlocal more
            dfs(node.left)
            if done:
                return
            if target > node.val:
                less = node.val
            if target <= node.val:
                more = node.val
                done = True
            dfs(node.right)
        dfs(root)
        if less == None:
            return more
        if more == None:
            return less
        if more - target < target - less:
            return more
        else:
            return less
