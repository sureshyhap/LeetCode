# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        answer = None
        flag = True
        def dfs(node):
            nonlocal answer
            nonlocal flag
            if not node or not flag:
                return
            left = dfs(node.left)
            right = dfs(node.right)
            this_node_matches = False
            if node.val == p.val or node.val == q.val:
                this_node_matches = True
            if (left and right) or (left and this_node_matches) or (this_node_matches and right):
                answer = node
                flag = False
                return
            if left:
                return left
            if right:
                return right
            if this_node_matches:
                return node
        dfs(root)
        return answer
