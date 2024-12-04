# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxLevelSum(self, root: Optional[TreeNode]) -> int:
        queue = deque([root])
        max_sum, result = root.val, 1 # lets say root level is max sum
        current_level = 1

        while queue:
            nodes_count = len(queue)
            current_sum = 0

            while nodes_count:
                node = queue.popleft()

                current_sum += node.val

                if node.left:
                    queue.append(node.left)

                if node.right:
                    queue.append(node.right)

                nodes_count -= 1

            if current_sum > max_sum:
                max_sum = current_sum
                result = current_level

            current_level += 1

        return result
        