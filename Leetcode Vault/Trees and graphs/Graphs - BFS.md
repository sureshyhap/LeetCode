Again it doesn't really matter if you use DFS or BFS with graphs. There are rarely scenarios where DFS performs better than BFS - people just choose DFS because it's faster/cleaner to implement, especially recursively.

But there are some problems where using BFS is clearly better than using DFS. In trees, this was the case when we were concerned with tree levels. In graphs, it is mostly the case when you are asked to find the **shortest path**.

Recall that in binary trees, BFS would visit all nodes at a depth `d` before visiting any node at a depth `d + 1`. BFS visited the nodes **according to their distance from the root.**

99% of the time, a graph will not have a tree structure. But even then, the same logic applies. Imagine whatever node you start from as a "root". Then, the neighbors of the root represent the next level, and the neighbors of those nodes represent the level after that.

BFS on a graph always visits nodes according to their distance from the **starting point**. This is the key idea behind BFS on graphs - **every time you visit a node**, you must have reached it in the minimum steps possible from wherever you started your BFS.

The above statement was always the case on binary trees, even if you did a DFS, because there is only one possible path to any node from the root. In a graph, there could be many paths from a given starting point to any other node. Using BFS will ensure that out of all possible paths, you take the shortest one.

We implemented DFS primarily with recursion, which uses a stack under the hood. To implement BFS, we will use a queue (iteratively) instead.

---------------------------------------------

Example 1: 1091 - Shortest Path in Binary Matrix

Given an `n x n` binary matrix `grid`, return the length of the shortest clear path in the matrix. If there is no clear path, return `-1`. A clear path is a path from the top-left cell `(0, 0)` to the bottom-right cell `(n - 1, n - 1)` such that all visited cells are `0`. You may move 8-directionally (up, down, left, right, or diagonally).

We can treat the matrix as a graph where each square is a node and all squares have up to 8 edges to adjacent squares (up to, because squares on the edges have less due to potential neighbors being out of bounds). There could be many paths on a matrix, but we want the shortest one. Remember: with traversals, we only want to visit each square at most once, not just for efficiency but also to avoid cycles. If were to do a DFS, we might not find the shortest path. Take the following example:

![[Pasted image 20241214104343.png]]

The path marked by the arrows is the optimal path (7 squares), and the red path is a path that might happen if you were to use DFS (11 squares). As you can see, the red path is longer and also "uses" up squares on the optimal path, and thus, this algorithm will not produce a correct answer. To find the shortest path, we should use BFS. With BFS, every time we visit a node, it is guaranteed that we reached it in the fewest steps possible.

Remember when we looked at BFS on trees, and every iteration of the while loop represented a level/depth? Think of the outward ripples that occur when a drop of water falls into a pool. The outward ripples are like the "levels" away from the initial node. Each level has the same distance from the start `(0, 0)` if you were to take the optimal path. With trees, we used a for loop inside of a while loop. This was because we cared about the levels as a whole - we wanted to analyze each level separately (find the maximum element, etc.). Here, we don't really care about the levels as a whole - we just want to reach the end `(n - 1, n - 1)`. As such, we don't need the for loop, just the while loop on a queue. We can store the number of steps we have taken with each node, and once we reach the bottom right we know that we have the answer. Recall that this is because the first time we visit a node with BFS, we know we must have reached it with the minimum possible steps.

Alternatively, you can keep using the format from the binary tree problems.

Then, you wouldn't need to store the number of steps taken so far with each node. You could initialize a variable `level` before starting the BFS and increment it every time you move up a level (each while loop iteration = one level). When you encounter the target node `(n - 1, n - 1)`, you can return `level`.

With BFS, **every time we visit a node, we must have arrived in the fewest possible steps**. When we reach the bottom right, its guaranteed that we did so in the fewest possible steps. If we associate the steps taken so far with each node, then we can immediately return once we reach the bottom right.

We store an extra integer with a node in each queue entry. When we get a `node` from the queue, we also get its `steps`. When we put the neighbors of `node` onto the queue, we also push `steps + 1`.

We use a helper function `valid` and a `directions` array to make the code cleaner, a good practice for all matrix graph problems. The BFS is identical to the iterative DFS implementations - each iteration in the while loop is handling a single node. The only difference between DFS and BFS is that we are using a queue instead of a stack.

```
from collections import deque

class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        if grid[0][0] == 1:
            return -1
        
        def valid(row, col):
            return 0 <= row < n and 0 <= col < n and grid[row][col] == 0
        
        n = len(grid)
        seen = {(0, 0)}
        queue = deque([(0, 0, 1)]) # row, col, steps
        directions = [(0, 1), (1, 0), (1, 1), (-1, -1), (-1, 1), (1, -1), (0, -1), (-1, 0)]
        
        while queue:
            row, col, steps = queue.popleft()
            if (row, col) == (n - 1, n - 1):
                return steps
            
            for dx, dy in directions:
                next_row, next_col = row + dy, col + dx
                if valid(next_row, next_col) and (next_row, next_col) not in seen:
                    seen.add((next_row, next_col))
                    queue.append((next_row, next_col, steps + 1))
        
        return -1
```

If the queue implementation is efficient, then removing from the left is $O(1)$ which makes the work at each node $O(1)$. This means the time complexity is equal to the number of nodes, which is $O(n^2)$. The space complexity is also $O(n^2)$ as `seen` can grow to that size.

With an efficient queue, BFS has the same time and space complexity as DFS.  The main difference is that we are using a queue instead of a stack.

---------------------------------------------

Example 2: 863 - All Nodes Distance K in Binary Tree

Given the `root` of a binary tree, a target node `target` in the tree, and an integer `k`, return an array of the values of all nodes that have a distance `k` from the target node.

In a binary tree, we only have pointers from parents to children. We can easily find the nodes at distance `k` that are in the target node's subtree, but what about all the other nodes? Let's convert the tree into a graph by assigning every node a `parent` pointer. Then, the tree becomes an undirected graph, and we can use a simple BFS to find the nodes at a distance `k`.

We can perform the parent assignments using either BFS or DFS - it doesn't really matter, so we'll use DFS. Then, we'll perform a BFS starting at `target`, and after we have reached `k` steps, we will return the nodes in the queue.

We are using the for loop inside the while loop again because this time we want **all** nodes on the kth level.

Note: in the Java and C++ implementations, we are using a hash map to remember the parents for each node. In Python and JavaScript, we are assigning a `parent` attribute to the node objects.

Assigning new attributes like this may be seen as a bad practice, and you should be careful doing so in an interview. The hash map may be considered the "safer" approach.

```
from collections import deque

class Solution:
    def distanceK(self, root: TreeNode, target: TreeNode, k: int) -> List[int]:
        def dfs(node, parent):
            if not node:
                return
            
            node.parent = parent
            dfs(node.left, node)
            dfs(node.right, node)
            
        dfs(root, None)
        queue = deque([target])
        seen = {target}
        distance = 0
        
        while queue and distance < k:
            current_length = len(queue)
            for _ in range(current_length):
                node = queue.popleft()
                for neighbor in [node.left, node.right, node.parent]:
                    if neighbor and neighbor not in seen:
                        seen.add(neighbor)
                        queue.append(neighbor)
            
            distance += 1
        
        return [node.val for node in queue]
```

Both the DFS and DFS perform constant work at each node, and only visit each node as most once. Therefore we have a time and space complexity of $O(n)$ (the space comes from the recursion call stack when we assign the parents, the queue, and `seen`).

---------------------------------------------

Example 3: 542 - 01 Matrix

Given an `m x n` binary (every element is `0` or `1`) matrix `mat`, find the distance to the nearest `0` for each cell. The distance between adjacent cells (horizontally or vertically) is `1`.

For example, given `mat = [[0,0,0],[0,1,0],[1,1,1]]`, return `[[0,0,0],[0,1,0],[1,2,1]]`.

For all `0`, the distance if `0`, so we don't need to change those. For all `1`, we need to find the nearest `0`. One way to solve this is to perform a BFS from each `1` that stops upon finding the first `0` - but this would be very inefficient. Imagine if you had a huge matrix with only `1`.  The time complexity would be $O(m^2 n^2)$ (each BFS costs $O(mn)$) and we would need to perform $O(mn)$ different BFS if the entire matrix is only `1`, except for a single `0` in a corner). Can we find a linear time approach that **avoids visiting the same square multiple times?**

Instead of performing the BFS from the ones, what if we started from the zeros? A critical observation is that if we have a square `x` with value `1` and its nearest square with value `0` is `y`, then it doesn't make a difference if we traverse from `x -> y` or `y -> x`, both take the same number of steps. If we perform a BFS starting from all the zeros, whenever we encounter a `1`, we know that the current number of steps is the answer for that `1`, Using `seen` will prevent the answer from being overridden. Here is a visualization:

![[Screenshot from 2025-01-02 09-18-57.png]]

![[Screenshot from 2025-01-02 09-19-19.png]]

![[Screenshot from 2025-01-02 09-19-46.png]]

Later on: 

![[Screenshot from 2025-01-02 09-20-36.png]]

![[Screenshot from 2025-01-02 09-20-50.png]]

In our BFS examples we have looked at so far in the course, we initialize the `queue` with only one node - the node we start our BFS from. The single node represented the $0^{th}$ level - the nodes that have a distance of `0` from the source. There is nothing stopping us from having multiple nodes in the $O^{th}$ level.

We said that with BFS, every time we visit a node, we do so in the fewest possible from the **source**.

The "source" is actually the $O^{th}$ level - not a single node. It's just that so far, we have only looked at problems where the $O^{th}$ level had only one node.

In this problem, we can have the "source" be any node with a value of `0`. We do this by initializing `queue` with all the `0` nodes. Again, we should associate the steps taken so far (the level) with each node. By the definition of BFS, every time we visit a node, we will have done so in the fewest steps possible from a `0`, which is exactly what the problem is asking for. By using `seen`, we will not override any shortest distances we have already found.

```
from collections import deque

class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        def valid(row, col):
            return 0 <= row < m and 0 <= col < n and mat[row][col] == 1
        
        # if you don't want to modify the input, you can create a copy at the start
        m = len(mat)
        n = len(mat[0])
        queue = deque()
        seen = set()
        
        for row in range(m):
            for col in range(n):
                if mat[row][col] == 0:
                    queue.append((row, col, 1))
                    seen.add((row, col))
        
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]

        while queue:
            row, col, steps = queue.popleft()
            
            for dx, dy in directions:
                next_row, next_col = row + dy, col + dx
                if (next_row, next_col) not in seen and valid(next_row, next_col):
                    seen.add((next_row, next_col))
                    queue.append((next_row, next_col, steps + 1))
                    mat[next_row][next_col] = steps
        
        return mat
```

One "bad" practice here is changing the input matrix. This leads to speedups but leads to side-effects of calling this function which can be hard to track and debug.

This algorithm improves the time complexity to $O(mn)$, because the BFS now only visits each square once, and does a constant amount of work each time. The space complexity is also $O(mn)$ for the queue and `seen`.

------------------------------------------

