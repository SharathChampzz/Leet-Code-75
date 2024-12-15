class Solution:
    def search(self, nums: List[int], target: int) -> int:
        # Initialize pointers for the left and right boundaries of the search
        left, right = 0, len(nums) - 1

        # Perform binary search
        while left <= right:
            mid = (left + right) // 2

            # Check if the middle element is the target
            if nums[mid] == target:
                return mid

            # Determine if the left half is sorted
            if nums[left] <= nums[mid]:
                # Check if the target is within the sorted left half
                if target >= nums[left] and target < nums[mid]:
                    right = mid - 1  # Narrow the search to the left half
                else:
                    left = mid + 1   # Narrow the search to the right half
            else:
                # The right half must be sorted
                # Check if the target is within the sorted right half
                if target > nums[mid] and target <= nums[right]:
                    left = mid + 1   # Narrow the search to the right half
                else:
                    right = mid - 1  # Narrow the search to the left half

        return -1 # target not found
