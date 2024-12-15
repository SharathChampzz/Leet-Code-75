# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        """
        Finds the maximum path sum in a binary tree.

        Args:
            root: The root of the binary tree.

        Returns:
            The maximum path sum.
        """
        self.max_sum = float('-inf')

        def dfs(node):
            """
            Performs depth-first search to calculate the maximum path sum through the node.

            Args:
                node: The current node.

            Returns:
                The maximum path sum from the node to its subtree.
            """
            if not node:
                return 0

            left_sum = max(dfs(node.left), 0)
            right_sum = max(dfs(node.right), 0)

            # Calculate the path sum through the current node
            current_path_sum = left_sum + right_sum + node.val

            # Update the global maximum sum
            self.max_sum = max(self.max_sum, current_path_sum)

            # Return the maximum path sum from the node to its subtree
            return node.val + max(left_sum, right_sum)

        dfs(root)
        return self.max_sum