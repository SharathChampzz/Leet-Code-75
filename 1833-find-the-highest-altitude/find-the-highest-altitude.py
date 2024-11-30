class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        current_height = 0
        max_height = 0

        for change in gain:
            current_height += (change)

            max_height = max(max_height, current_height)

        return max_height

        