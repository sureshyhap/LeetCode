# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deepestLeavesSum(self, root: Optional[TreeNode]) -> int:
        from collections import deque
        from copy import copy
        queue = deque([root])
        while queue:
            nodes_at_level = len(queue)
            queue_copy = queue.copy()
            some_node_had_children = False
            for _ in range(nodes_at_level):
                node = queue.popleft()
                if node.left:
                    queue.append(node.left)
                    some_node_had_children = True
                if node.right:
                    queue.append(node.right)
                    some_node_had_children = True
            if not some_node_had_children:
                return sum([node.val for node in queue_copy])
                
