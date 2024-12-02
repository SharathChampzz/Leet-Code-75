# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def goodNodes(self, root: TreeNode) -> int:

        def search_node(node, current_max):
            if not node:
                return 0

            new_max = max(current_max, node.val)
            
            left_nodes = search_node(node.left, new_max)
            right_nodes = search_node(node.right, new_max)

            return left_nodes + right_nodes + (1 if node.val >= current_max else 0)

        answer = search_node(root, root.val)

        return answer
        