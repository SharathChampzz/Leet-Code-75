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
                return count - 1  # Reached a leaf node, return the count minus one

            if prev_direction == -1:
                # Prev direction was to the left, next right path will have count + 1
                # If going left again, reset the count to 1
                right_count = dfs(node.right, count + 1, 1)
                left_count = dfs(node.left, 1, -1)  # Reset the count to 1
            else:
                # Prev direction was to the right, next left path will have count + 1
                # If going right again, reset the count to 1
                right_count = dfs(node.right, 1, 1)  # Reset the count to 1
                left_count = dfs(node.left, count + 1, -1)

            return max(left_count, right_count)

        # Handle left and right separately since the root node has no previous direction
        left_count = dfs(root.left, 1, -1)
        right_count = dfs(root.right, 1, 1)

        return max(left_count, right_count)
