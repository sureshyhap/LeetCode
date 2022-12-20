class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.k = k
        self.heap = []
        self.heap2 = []
        if nums:
            self.heap = list(map(lambda x : -x, nums))
            heapq.heapify(self.heap)
            for _ in range(self.k - 1):
                value2 = -heapq.heappop(self.heap)
                heapq.heappush(self.heap2, value2)



    def add(self, val: int) -> int:
        if self.heap:
            top = -self.heap[0]
            if val < top:
                heapq.heappush(self.heap, -val)
            else:
                heapq.heappush(self.heap2, val)
                new_kth = -heapq.heappop(self.heap2)
                heapq.heappush(self.heap, new_kth)
        else:
            self.heap.append(-val)
            if self.heap2:
                top2 = self.heap2[0]
                top = -self.heap[0]
                if top > top2:
                    value = -heapq.heappop(self.heap)
                    heapq.heappush(self.heap2, value)
                    minimum = heapq.heappop(self.heap2)
                    heapq.heappush(self.heap, -minimum)
        return -self.heap[0]



# Your KthLargest object will be instantiated and called as such:
# obj = KthLargest(k, nums)
# param_1 = obj.add(val)
