class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        """
        Code Flow:
            Set the left and right pointer to zero and keep expanding right pointer.
            If any zero occur, increment zero count making sure it is not beyond allowed "k"
            If zero count is more, we need to get rid off first zero, So the left pointer next to it.
            For every iteration, calculate the max length
        """
        left = 0
        zero_count = 0
        max_len = 0

        for right in range(len(nums)):
            if nums[right] == 0:
                zero_count += 1

            while zero_count > k:
                if nums[left] == 0:
                    zero_count -= 1
                left += 1

            max_len = max(max_len, right - left + 1)

        return max_len