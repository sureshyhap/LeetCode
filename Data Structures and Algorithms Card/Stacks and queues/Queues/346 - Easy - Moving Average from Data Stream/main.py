class MovingAverage:

    from collections import deque

    def __init__(self, size: int):
        self.window_size = size
        self.stream = deque()
        self.sum = 0

    def next(self, val: int) -> float:
        self.stream.append(val)
        self.sum += val
        if len(self.stream) <= self.window_size:
            return self.sum / len(self.stream)
        self.sum -= self.stream[0]
        self.stream.popleft()
        return self.sum / self.window_size
        


# Your MovingAverage object will be instantiated and called as such:
# obj = MovingAverage(size)
# param_1 = obj.next(val)
