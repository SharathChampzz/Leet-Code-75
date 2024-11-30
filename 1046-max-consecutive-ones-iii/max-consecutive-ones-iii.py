class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
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











    def longestOnesMod(self, nums: List[int], k: int) -> int:
        left = 0
        flip_rem = k # flips remaining count

        max_len = 0 # init result

        for right in range(len(nums)):
            if nums[right] == 0 and flip_rem > 0:
                flip_rem -= 1
            elif nums[right] == 0:
                while nums[left] == 1 and left < len(nums):
                    left += 1 # move the pointer till zero
                left += 1 # skip the current zero

            max_len = max(max_len, right - left + 1)

        return max_len

            
        