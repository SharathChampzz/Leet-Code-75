class Solution:
    def findPeakElement(self, nums: List[int]) -> int:

        s = sorted(enumerate(nums), key= lambda x: x[1])
        # print(s)

        return s[-1][0]
        