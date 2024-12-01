class RecentCounter:

    def __init__(self):
        self.counter = deque([]) # using dequeue, it is easy to add new elements and remove older unwanted elements

    def ping(self, t: int) -> int:
        self.counter.append(t)

        while (t - self.counter[0]) > 3000:
            self.counter.popleft() # remove all the requests that are older than 3000

        return len(self.counter)       


# Your RecentCounter object will be instantiated and called as such:
# obj = RecentCounter()
# param_1 = obj.ping(t)