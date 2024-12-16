from typing import List

class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        if not nums:
            return 0

        # Step 1: Initialize DP array
        dp = [1] * len(nums)

        # Step 2: Fill DP array
        for i in range(1, len(nums)):
            for j in range(i):
                if nums[j] < nums[i]:
                    dp[i] = max(dp[i], dp[j] + 1)

        # Step 3: Find the maximum length
        return max(dp)
       
# solving using backtracking
class BackTrackingSolution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        def backtrack(idx, prev):
            if idx == len(nums):
                return 0

            # Not choose current element
            res = backtrack(idx + 1, prev)

            # Choose current element if it's greater than previous
            if prev < nums[idx]:
                res = max(res, 1 + backtrack(idx + 1, nums[idx]))

            return res

        return backtrack(0, float('-inf'))
