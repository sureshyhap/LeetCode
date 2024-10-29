# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        from collections import deque
        queue = deque([root])
        answer = []
        level_id = 0
        while queue:
            nodes_at_level = len(queue)
            level = []
            if level_id % 2 == 0:
                for i in range(nodes_at_level):
                    level.append(queue[i].val)
            else:
                for i in range(nodes_at_level - 1, -1, -1):
                    level.append(queue[i].val)
            answer.append(level)
            level_id += 1
            for _ in range(nodes_at_level):
                node = queue.popleft()
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
        return answer
