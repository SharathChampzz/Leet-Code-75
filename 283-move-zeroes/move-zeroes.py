class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        slow_p, fast_p = 0, 0
        n = len(nums)

        while fast_p < n:
            current_num = nums[fast_p]

            if current_num != 0:
                nums[slow_p] = current_num
                slow_p += 1

            fast_p += 1

        while slow_p < n:
            nums[slow_p] = 0 # set 0 to rest of numbers
            slow_p += 1

        