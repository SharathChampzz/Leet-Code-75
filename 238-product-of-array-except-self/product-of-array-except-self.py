class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        """
        Logic:
            Basically, here we need to calculate product of full array except self element
            which means, we need to calculate the product of all left items and right items, (leaving the current element)

            So in first iteration, calculate product of left items
            and in second iteration, calculate right product and multiply with already calculated left prod values. 
            or 
            To make code look easier, you can create two separate left and right prod arrays and multiply later
        """
        n = len(nums)
        result = [1] * n

        for i in range(1, n):
            result[i] = result[i-1] * nums[i-1]

        right_prod = 1
        for j in range(n-1, -1, -1):
            result[j] *= right_prod
            right_prod *= nums[j]

        return result

        