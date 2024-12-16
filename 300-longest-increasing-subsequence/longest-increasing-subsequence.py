from typing import List

class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        n = len(nums)
        dp = [1] * n

        for i in range(n - 2, -1, -1):
            for j in range(i+1, n):
                if nums[j] > nums[i]:
                    dp[i] = max(dp[i], dp[j] + 1)
                    # break

        print(dp)
        return max(dp)
        

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
