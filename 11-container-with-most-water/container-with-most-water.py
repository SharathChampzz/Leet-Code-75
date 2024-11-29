class Solution:
    def maxArea(self, height: List[int]) -> int:
        """
        Area = Height * Breadth 
        To get maximum area, we need vertical lines of maximum height and maximum distance (breadth)

        Looking at the diagram and as we need to find range of index, We can try Two Pointer

        To get maximum height, we however need to iterate through all the heights. 
        But atleast we can try considering maximum breadth by placing the pointers at the corners and move inside as we progress
        """
        n = len(height)
        result = 0

        left, right = 0, n-1

        while left < right:
            current_capacity = min(height[left], height[right]) * (right - left)
            result = max(result, current_capacity)

            # To achieve the maximum result, move the pointer with the smaller height.
            # Moving the pointer with the greater height is ineffective
            # because we need to increase min(height[left], height[right]).
            # If we move the pointer with the greater height, we will still get the same old height or even less.

            if height[left] < height[right]:
                left += 1
            else:
                right -= 1

        return result

        