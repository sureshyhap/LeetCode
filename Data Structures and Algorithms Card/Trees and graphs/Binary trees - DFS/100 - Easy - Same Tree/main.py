# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        def dfs(root1, root2):
            if not root1 and not root2:
                return True
            elif not root1 or not root2:
                return False
            left = dfs(root1.left, root2.left)
            right = dfs(root1.right, root2.right)
            return (root1.val == root2.val) and left and right
        return dfs(p, q)
        """
        if not p and not q:
            return True
        if not p or not q:
            return False
        stack1 = [p]
        stack2 = [q]
        while stack1 and stack2:
            first = stack1.pop()
            second = stack2.pop()
            if first and second:
                if first.val != second.val:
                    return False
            elif not first and not second:
                continue
            else:
                return False
            stack1.append(first.left)
            stack1.append(first.right)
            stack2.append(second.left)
            stack2.append(second.right)
        if stack1 or stack2:
            return False
        return True
        """
