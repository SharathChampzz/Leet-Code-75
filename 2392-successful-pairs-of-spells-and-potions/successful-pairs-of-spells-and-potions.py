
class Solution:
    def successfulPairs(self, spells: List[int], potions: List[int], success: int) -> List[int]:
        # Sort potions to use binary search
        potions.sort()
        result = []

        for spell in spells:
            # Binary search to find the first potion that forms a successful pair
            left, right = 0, len(potions)
            while left < right:
                mid = (left + right) // 2
                if spell * potions[mid] >= success:
                    right = mid
                else:
                    left = mid + 1

            # The number of successful pairs for the current spell
            result.append(len(potions) - left)

        return result
