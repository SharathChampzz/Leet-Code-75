class SmallestInfiniteSet:

    def __init__(self):
        # here we are popping least value, so least number has more priority
        # lets use priority queue -- heap data structure
        self.heap_size = self.current_max = 10
        self.heap = [i for i in range(1, self.heap_size+1)] # for faster search to check
        heapq.heapify(self.heap) # now whenever we pop we get least value

    def popSmallest(self) -> int:
        if len(self.heap) < self.heap_size:
            self.current_max += 1
            heapq.heappush(self.heap, self.current_max) # add new number to the end
        return heapq.heappop(self.heap)

    def addBack(self, num: int) -> None:
        if num < self.current_max and num not in self.heap:
            heapq.heappush(self.heap, num)


# Your SmallestInfiniteSet object will be instantiated and called as such:
# obj = SmallestInfiniteSet()
# param_1 = obj.popSmallest()
# obj.addBack(num)