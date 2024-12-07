
class SmallestInfiniteSet:
    def __init__(self):
        """
        Initialize the SmallestInfiniteSet object.
        We use a priority queue (min-heap) to keep track of the smallest available numbers.
        """
        self.min_heap = []  # Min-heap to store the smallest available numbers
        self.current_max = 0  # Current maximum number in the set
        self.in_heap = set()  # Set to track numbers in the heap

    def popSmallest(self) -> int:
        """
        Remove and return the smallest number from the set.
        If the heap is empty, increment the current maximum and return it.
        """
        if self.min_heap:
            smallest = heapq.heappop(self.min_heap)
            self.in_heap.remove(smallest)
            return smallest
        else:
            self.current_max += 1
            return self.current_max

    def addBack(self, num: int) -> None:
        """
        Add a number back into the set if it is not already present and is less than the current maximum.
        """
        if num <= self.current_max and num not in self.in_heap:
            heapq.heappush(self.min_heap, num)
            self.in_heap.add(num)

# Little bit different approach, where size will be already initialized 
class SmallestInfiniteSetPredefinedSize:
    def __init__(self):
        """
        Initialize the SmallestInfiniteSet object.
        We use a priority queue (min-heap) to keep track of the smallest available numbers.
        """
        self.heap_size = 10  # Initial size of the heap
        self.current_max = 10  # Current maximum number in the set
        self.heap = [i for i in range(1, self.heap_size + 1)]  # Initialize the heap with numbers 1 to 10
        heapq.heapify(self.heap)  # Transform the list into a heap

    def popSmallest(self) -> int:
        """
        Remove and return the smallest number from the set.
        If the heap size is less than the initial size, add the next number to the heap.
        """
        if len(self.heap) < self.heap_size:
            self.current_max += 1
            heapq.heappush(self.heap, self.current_max)  # Add the next number to the heap
        return heapq.heappop(self.heap)  # Pop and return the smallest number

    def addBack(self, num: int) -> None:
        """
        Add a number back into the set if it is not already present and is less than the current maximum.
        """
        if num < self.current_max and num not in self.heap:
            heapq.heappush(self.heap, num)  # Add the number back to the heap



# Your SmallestInfiniteSet object will be instantiated and called as such:
# obj = SmallestInfiniteSet()
# param_1 = obj.popSmallest()
# obj.addBack(num)