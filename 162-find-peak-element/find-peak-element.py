class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        # sort and get the last element
        # but we need to return index so enumerate (index, val) and then sort based on val
        return sorted(enumerate(nums), key= lambda x: x[1])[-1][0] # return last element and index
        