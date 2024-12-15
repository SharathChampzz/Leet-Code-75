class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        max_sum = current_sum = nums[0]

        # kadane's algorithm
        for num in nums[1:]:
            current_sum = max(num, current_sum + num)
            print(current_sum)
            max_sum = max(max_sum, current_sum)       

        return max_sum


        