"""

Given the root of a binary tree, imagine yourself standing on the right side of it, return the values of the nodes you can see ordered from top to bottom.

 
Example 1:

Input: root = [1,2,3,null,5,null,4]
Output: [1,3,4]

Example 2:

Input: root = [1,2,3,4,null,null,null,5]
Output: [1,3,4,5]

Example 3:

Input: root = [1,null,3]
Output: [1,3]

Example 4:

Input: root = []
Output: []

Time Complexity:
- Method 1: O(N) since each node is processed once.
- Method 2: O(N) since all nodes are stored in a list before processing.

Space Complexity:
- Method 1: O(N) due to queue storage.
- Method 2: O(N) due to both queue and temporary list storage.

Did this code successfully run on Leetcode : Yes
Any problem you faced while coding this : No

"""

# Approach:
# performed a level-order traversal using a queue and store the last node of each level in the result list.
# The first method processes nodes directly from the queue, adding only the last node’s value for each level.
# The second method stores all nodes of a level in a temporary list before extracting the last node’s value.

from queue import Queue

# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        
        # Method 1
        q = Queue()
        q.put(root)

        res = []

        while not q.empty():
            size = q.qsize()
            for i in range(size):
                ele = q.get()
                if ele is not None:
                    if i == size - 1:
                        res.append(ele.val)
                    if ele.left:
                        q.put(ele.left)
                    if ele.right:
                        q.put(ele.right)
        
        return res

        # Method 2
        if not root:
            return []

        q = Queue()
        q.put(root)

        res = []

        while not q.empty():
            size = q.qsize()
            level_nodes = []
            for i in range(size):
                ele = q.get()
                level_nodes.append(ele)
            
            ele = level_nodes[-1]
            res.append(ele.val)

            for node in level_nodes:
                if node.left:
                    q.put(node.left)
                if node.right:
                    q.put(node.right)
    
        return res
