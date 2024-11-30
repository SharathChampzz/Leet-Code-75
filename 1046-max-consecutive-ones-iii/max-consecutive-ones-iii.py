class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        left = 0
        flip_rem = k # flips remaining count

        max_len = 0

        for right in range(len(nums)):
            if nums[right] == 0 and flip_rem > 0:
                flip_rem -= 1
            elif nums[right] == 0:
                while nums[left] == 1 and left < len(nums):
                    left += 1 # move the pointer till zero
                left += 1 # skip the current zero
                # flip_rem += 1 # as we moved left pointer to next of first zero

            max_len = max(max_len, right - left + 1)
            # print(f'max_len: {max_len} for left: {left} and right: {right} => flip_rem: {flip_rem}')

        return max_len

            
        