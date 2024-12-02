# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def leafSimilar(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        
        def get_leaf_nodes(root):
            if not root:
                return []
            
            if not root.left and not root.right:
                return [root.val]

            left_leaf_nodes = get_leaf_nodes(root.left)
            right_leaf_nodes = get_leaf_nodes(root.right)

            return left_leaf_nodes + right_leaf_nodes

        left = get_leaf_nodes(root1)
        right = get_leaf_nodes(root2)

        print(left)
        print(right)

        return left == right
        