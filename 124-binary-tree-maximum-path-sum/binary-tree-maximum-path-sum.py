# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        result = root.val

        def dfs(node) -> int:
            nonlocal result
            if not node:
                return 0

            left_sum = dfs(node.left)
            right_sum = dfs(node.right)
            total = left_sum + right_sum + node.val

            result = max([result, total, node.val, node.val + left_sum, node.val + right_sum])
            print(f'total sum for parent node {node.val} is {total} ({left_sum} + {right_sum} + {node.val}) and current_max is {result}')

            return max(node.val, node.val + left_sum, node.val + right_sum)

        dfs(root)

        return result

        
        