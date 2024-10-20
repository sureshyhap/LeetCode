# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxAncestorDiff(self, root: Optional[TreeNode]) -> int:
        answer = 0
        def dfs(node):
            if not node:
                return None, None
            
            left_min, left_max = dfs(node.left)
            right_min, right_max = dfs(node.right)
            minimum, maximum = None, None

            if left_min != None and right_min != None:
                minimum = min(left_min, right_min)
            elif left_min != None:
                minimum = left_min
            elif right_min != None:
                minimum = right_min
            else:
                return node.val, node.val

            if left_max != None and right_max != None:
                maximum = max(left_max, right_max)
            elif left_max != None:
                maximum = left_max
            elif right_max != None:
                maximum = right_max
            else:
                return node.val, node.val
            
            nonlocal answer
            answer = max(answer, abs(node.val - minimum), abs(node.val - maximum))
            return min(node.val, minimum), max(node.val, maximum)

        dfs(root)
        return answer
