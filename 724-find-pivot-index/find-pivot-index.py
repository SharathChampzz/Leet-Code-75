class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        total_sum = sum(nums)
        left_sum = 0

        """
            total_sum = left_sum + pivot + right_sum
            total_sum = left_sum + pivot + left_sum # because left_sum == right_sum
            total_sum = 2*left_sum + pivot
            left_sum = (total_sum - num) / 2
            Let's calculate different left_sum and check where it leads to the current expression.
        """

        for i, pivot in enumerate(nums):
            if left_sum == (total_sum - pivot) / 2:
                return i
            left_sum += pivot

        return -1
        