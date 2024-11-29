class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        count_mapping = defaultdict(int)
        op_count = 0 # result operation count

        for num in nums:
            compliment = k - num

            if count_mapping[compliment]: # it should exist and it should not be zero
                count_mapping[compliment] -= 1
                op_count += 1
            else:
                count_mapping[num] += 1

        return op_count