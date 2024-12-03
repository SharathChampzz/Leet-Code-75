# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def longestZigZag(self, root: Optional[TreeNode]) -> int:

        def dfs(node, count, prev_direction):
            if not node:
                return count - 1 # reached leaf node, 

            if prev_direction == -1:
                # if we are coming from the left, next right path will have the count + 1
                # but if we are coming from the left, and if we are going again to the left we have to reset count
                right_count = dfs(node.right, count + 1, 1)
                left_count = dfs(node.left, 1, -1) # reset the count to 1
            else:
                right_count = dfs(node.right, 1, 1) # reset the count to 1
                left_count = dfs(node.left, count + 1, -1)

            return max(left_count, right_count)

        # we cannot directly pass root node, because it has no prev_direction
        # so we need handle left and right separately
        left_count = dfs(root.left, 1, -1)
        right_count = dfs(root.right, 1, 1)

        return max(left_count, right_count)


        