# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        # keep track of bigger number during traversal
        # if current_val is smaller than already visited bigger number it means it is not good node
        # if current_val is equal or greather than already visited numbers or that big number. It can be considered as good node
        # So to calculate, you will left good nodes, right good nodes and you should also consider the current node

        # Key point in tree problems is, you need to break down the big problem into root, left and right and start analysing it.

        def get_good_nodes_count(node, current_max):
            if not node:
                return 0

            new_max = max(current_max, node.val)
            
            left_nodes  = get_good_nodes_count(node.left, new_max)
            right_nodes = get_good_nodes_count(node.right, new_max)

            return left_nodes + right_nodes + (1 if node.val >= current_max else 0) # left + right + current_root

        return get_good_nodes_count(root, root.val)
        