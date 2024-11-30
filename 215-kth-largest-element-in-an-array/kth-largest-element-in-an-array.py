class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        heap = []

        for num in nums:
            heapq.heappush(heap, num)

            if len(heap) > k:
                heapq.heappop(heap)

        return heapq.heappop(heap)

    def findKthLargestUsingMaxHeap(self, nums: List[int], k: int) -> int:
        """Solved using Max Heap"""
        for i in range(len(nums)):
            nums[i] *= -1 # multiply by -1 to build max heap

        heapq.heapify(nums) # max heap

        while k != 1:
            heapq.heappop(nums)
            k -= 1

        return -1 * heapq.heappop(nums)

    def findKthLargestUsingMinHeap(self, nums: List[int], k: int) -> int:
        """Solved using Min Heap"""
        heapq.heapify(nums)

        while len(nums) != k:
            heapq.heappop(nums)

        return heapq.heappop(nums)
        