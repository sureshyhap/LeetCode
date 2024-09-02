**Monotonic**: (of a function or quantity) varying in such a way that it either never decreases or never increases.

A monotonic stack or queue is one whose elements are always sorted (either by ascending or descending order). Monotonic stacks and queues maintain their sorted property by removing elements that would violate the property before adding new elements. For example, let's say you had a monotonically increasing stack, currently `stack = [1, 5, 8, 15, 23]`. You want to push `14` onto the stack. To maintain the sorted property, we need to first pop the `15` and `23` before pushing the `14` - after the push operation, we have `stack = [1, 5, 8, 14]`.

Here is some pseudocode for a monotonic increasing stack:

```
Given an integer array nums

stack = []
for num in nums:
    while stack.length > 0 AND stack.top >= num:
        stack.pop()
    // Between the above and below lines, do some logic depending on the problem
    stack.push(num)
```

Before we push a `num` onto the stack, we first check if the monotonic property would be violated, and pop elements until it won't be.

Despite the nested loop, the time complexity is $O(n)$ where $n$ is the length of the array because collectively can't push and pop more elements that are in the array. 

Monotonic stacks and queues are useful in problems that for each element, involves finding the "next" element based on some criteria, for example, the next greater element. They're also good when you have a dynamic window of elements and you want to maintain knowledge of the maximum or minimum elements as the window changes. Sometimes a monotonic stack or queue is only one part of the entire algorithm.

-----------------------------------

Example 1: 739 - Daily Temperatures

Given an array of integers `temperatures` that represents the daily temperatures, return an array `answer` such that `answer[i]` is the number of days you have to wait after the ith day to get a warmer temperature. If there is no future day that is warmer, have `answer[i] = 0` instead.

The brute force approach would be to iterate over the input, and for each temperature, iterate through the rest of the array until we find a warmer temperature. Let's say we had `temperatures = [34, 33, 32, 31, 30, 50]`. The first 5 days all share the same "answer" day, the 6th day. Can we leverage this fact to improve from an $O(n^2)$ time complexity?

The second element `33` is not warmer than the first element `34`. The third element `32` is not warmer than the second element `33`. This property is transitive, and it implies that the third element is not warmer than the first element (32 <= 33 <= 34). This means that there's no point in worrying about the first element until we have found a warmer temperature than the second element because any temperature that isn't warmer than the second element is also not warmer than the first element.

This logic of handling elements in backward order reminds us of a stack. We can push the temperatures onto a stack, and pop them off once we find a warmer temperature. Let's look at another example, `temperatures = [40, 35, 32, 37, 50]`. Once we get to the 4th element, we have `stack = [40, 35, 32]`. Now, we see that `37 > 32` and `37 > 35`, so we can pop both of them off the stack. This leaves us with `stack = [40, 37]` after pushing the `37`. At the `50`, we can pop both elements off the stack because `50` is a greater than both of them.

Because the stack is monotonically decreasing, we are guaranteed to pop elements only when we find the first warmer temperature.

The problem wants the distance between elements, so we can store the indices instead of the actual temperatures.

Essentially, the stack holds temperatures that we have not yet found a warmer temperature for. Because we are forcing it to be monotonically decreasing, the temperature at the top of the stack will always be the coldest one.

```
class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = []
        answer = [0] * len(temperatures)
        
        for i in range(len(temperatures)):
            while stack and temperatures[stack[-1]] < temperatures[i]:
                j = stack.pop()
                answer[j] = i - j
            stack.append(i)
        
        return answer
```

Here, monotonically non-increasing would be a more accurate term than monotonically decreasing because we could have elements in the stack with equal temperatures in this problem.

--------------------------------

Example 2: 239 - Sliding Window Maximum

Given an integer array `nums` and an integer `k`, there is a sliding window of size `k` that moves from the very left to the very right. For each window, find the maximum element in the window.

For example, given `nums = [1, 3, -1, -3, 5, 3, 6, 7], k = 3`, return `[3, 3, 5, 5, 6, 7]`. The first window is [1, 3, -1] and the last window is [3, 6, 7].

It's easy to know what the maximum number if for a given window. You can just record it when you build it. The difficult part is, when the maximum number leaves the window, how do you know what is the second largest? When that number leaves, what's next?

We are concerned about the largest elements. We want to store the elements in a way that when the maximum element is removed, we know the second maximum, and when that element is removed, we know the third maximum, and so forth. This should also be updated in new elements being added. 
