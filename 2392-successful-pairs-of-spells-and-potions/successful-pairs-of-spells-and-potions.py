class Solution:
    def successfulPairs(self, spells: List[int], potions: List[int], success: int) -> List[int]:
        m, n = len(spells), len(potions)
        # spells.sort()
        potions.sort()
        result = []

        for i in range(m):
            current_spell = spells[i]
            left, right = 0, n-1
            while left < right:
                mid = (left + right) // 2
                prod = current_spell * potions[mid]

                if prod >= success:
                    right = mid
                else:
                    left = mid + 1

            result.append(n-left) if (current_spell * potions[left]) >= success else result.append(0)

        return result


        