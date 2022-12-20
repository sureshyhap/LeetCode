class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.k = k
        self.data = nums

    def add(self, val: int) -> int:
        self.data.append(val)
        return self.quick_select(0, len(self.data) - 1, self.k)
        
    def quick_select(self, start_index, end_index, k):
        
        
        
        if end_index - start_index >= 2:
            mid = self.median_3_part(start_index, end_index)
            pivot = self.data[mid]
            self.swap(mid, end_index - 1)
            start = start_index
            end = end_index - 1
            while start < end:
                start += 1
                while self.data[start] > pivot:
                    start += 1
                end -= 1
                while self.data[end] < pivot:
                    end -= 1
                if start < end:
                    self.swap(start, end)
            self.swap(start, end_index - 1)
            if start == k:
                return self.data[start]
            elif k > start:
                return self.quick_select(start + 1, end_index - 1, k)
            else:
                return self.quick_select(start_index, start - 1, k)
        else:
            if start_index == k:
                return self.data[start_index]
            elif end_index == k:
                return self.data[end_index]
        
        
        
        
        
    def median_3_part(self, start, end):
        first = start
        last = end
        mid = (first + last) // 2
        if self.data[first] < self.data[mid]:
            self.swap(first, mid)
        if self.data[first] < self.data[last]:
            self.swap(first, last)
        if self.data[mid] < self.data[last]:
            self.swap(mid, last)
        return mid
            
    def swap(self, index1, index2):
        temp = self.data[index1]
        self.data[index1] = self.data[index2]
        self.data[index2] = temp


# Your KthLargest object will be instantiated and called as such:
# obj = KthLargest(k, nums)
# param_1 = obj.add(val)
