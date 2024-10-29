# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
        answer = 0
        stack = [root]
        while stack:
            node = stack.pop()
            curr = node.val
            answer += (curr if low <= curr <= high else 0)
            if node.right and node.val < high:
                stack.append(node.right)
            if node.left and node.val > low:
                stack.append(node.left)
        return answer
        """
        answer = 0
        done = False
        def dfs(node):
            nonlocal done
            if node == None or done:
                return
            nonlocal answer
            dfs(node.left)
            if node.val >= low:
                if node.val <= high:
                    answer += node.val
                if node.val > high:
                    done = True
            dfs(node.right)
        dfs(root)
        return answer
        """
