class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        current_max = max(candies)

        return [(candy + extraCandies) >= current_max for candy in candies]
        