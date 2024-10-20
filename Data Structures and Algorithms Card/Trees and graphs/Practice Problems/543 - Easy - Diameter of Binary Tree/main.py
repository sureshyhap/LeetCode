# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        max_diameter = 0
        def dfs(root, depth):
            if not root:
                return
            left_depth = dfs(root.left, depth + 1)
            right_depth = dfs(root.right, depth + 1)

            potential_longest_path = 0
            if left_depth != None and right_depth != None:
                potential_longest_path = (left_depth - depth) + (right_depth - depth)
            elif left_depth != None:
                potential_longest_path = (left_depth - depth)
            elif right_depth != None:
                potential_longest_path = (right_depth - depth)
            else:
                return depth

            nonlocal max_diameter
            max_diameter = max(max_diameter, potential_longest_path)
            if left_depth != None and right_depth != None:
                return max(left_depth, right_depth)
            elif left_depth != None:
                return left_depth
            elif right_depth != None:
                return right_depth
                
        dfs(root, 0)
        return max_diameter
