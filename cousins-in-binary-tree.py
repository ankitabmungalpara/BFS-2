"""

Given the root of a binary tree with unique values and the values of two different nodes of the tree x and y, return true if the nodes corresponding to the values x and y in the tree are cousins, or false otherwise.

Two nodes of a binary tree are cousins if they have the same depth with different parents.

Note that in a binary tree, the root node is at the depth 0, and children of each depth k node are at the depth k + 1.

Example 1:

Input: root = [1,2,3,4], x = 4, y = 3
Output: false

Example 2:

Input: root = [1,2,3,null,4,null,5], x = 5, y = 4
Output: true

Example 3:

Input: root = [1,2,3,null,4], x = 2, y = 3
Output: false

Time Complexity:
DFS: O(N) - We visit each node once.
BFS: O(N) - We process each node once in the queue.

Space Complexity:
DFS: O(H) - The recursion stack can go up to the height of the tree (O(logN) for balanced, O(N) for skewed trees).
BFS: O(W) - The queue stores at most one level of nodes, where W is the maximum width of the tree.


Did this code successfully run on Leetcode : Yes
Any problem you faced while coding this : No

"""

# Approach:
# used both DFS (recursive) and BFS (iterative) to find the depth and parent of nodes x and y.
# In DFS, traversed the tree recursively, updating parent and depth when we find x or y.
# In BFS, used a queue to process nodes level by level, tracking parent and depth in a breadth-first manner.

from queue import Queue


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isCousins(self, root: Optional[TreeNode], x: int, y: int) -> bool:

        # Method 1: DFS Approach
      
        parent_x, parent_y = None, None
        d_x, d_y = None, None

        def dfs(root, p, d):
            nonlocal parent_x, parent_y, d_x, d_y

            if not root:
                return 
            if root.val == x:
                parent_x = p
                d_x = d
                
            if root.val == y:
                parent_y = p
                d_y = d
                
            dfs(root.left, root, d+1)
            dfs(root.right, root, d+1)

        dfs(root, None, 0)

        return parent_x != parent_y and d_x == d_y

        # Method 2: BFS Approach
      
        parent_x, parent_y = None, None
        d_x, d_y = None, None

        q = Queue()
        if not root:
            return False
        
        q.put((root, None, 0))

        while not q.empty():
            size = q.qsize()
            for _ in range(size):
                ele, p, d = q.get()
 
                if ele.val == x:
                    parent_x = p
                    d_x = d
                    
                if ele.val == y:
                    parent_y = p
                    d_y = d
                
                if ele.left:
                    q.put((ele.left, ele, d+1))
                if ele.right:
                    q.put((ele.right, ele, d+1))

        return parent_x != parent_y and d_x == d_y

