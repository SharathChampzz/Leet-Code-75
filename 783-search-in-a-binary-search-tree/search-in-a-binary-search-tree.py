# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def searchBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        """
            Properties of a BST:
                Left Subtree: All nodes in the left subtree have values less than the root node.

                Right Subtree: All nodes in the right subtree have values greater than the root node.

                No Duplicates: Typically, BSTs do not contain duplicate values.
        """

        while root:
            if val == root.val:
                return root
            elif val > root.val:
                root = root.right
            else:
                root = root.left

        # return None # by default this will be returned, we dont need this ideally