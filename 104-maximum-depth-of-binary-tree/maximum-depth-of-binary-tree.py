# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        max_depth = 0

        def calc(root, current_depth):
            nonlocal max_depth
            if root:
                max_depth = max(max_depth, current_depth + 1)
                calc(root.left, current_depth + 1)
                calc(root.right, current_depth + 1)

        calc(root, 0)

        return max_depth
        