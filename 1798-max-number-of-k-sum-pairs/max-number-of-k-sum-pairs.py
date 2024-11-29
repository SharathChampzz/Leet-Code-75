class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        n = len(nums)
        left, right = 0, n-1
        op_count = 0

        nums.sort()

        while left < right:
            current_sum = nums[left] + nums[right]

            if current_sum == k:
                left += 1
                right -= 1
                op_count += 1
            elif current_sum > k:
                right -= 1
            else:
                left += 1

        return op_count


    def maxOperationsTwo(self, nums: List[int], k: int) -> int:
        """
            We need to find pair-sum, So it is like two sum problem, where we can levarage compliment to find missing number

            This problem can be solved using two approach:
                #1. Two pointer -- For this you will have to sort the array.
                #2. Using compliment sum -- Current problem is solved using it.
        """
        count_mapping = defaultdict(int)
        op_count = 0 # result operation count

        for num in nums:
            compliment = k - num

            if count_mapping[compliment]: # if compliment exist and it should not be zero
                count_mapping[compliment] -= 1
                op_count += 1 # remove compliment and dont add the new number
            else:
                count_mapping[num] += 1

        return op_count