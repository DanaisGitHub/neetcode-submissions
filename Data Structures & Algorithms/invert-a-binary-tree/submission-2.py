# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        # for every node you're about to put into quue

        queue = deque()
        if root:
            queue.append(root)
        
        while queue:
            currQueue = queue.popleft()
            
            tempStore = currQueue.left
            currQueue.left = currQueue.right
            currQueue.right = tempStore
            
            if currQueue.left:
                queue.append(currQueue.left)
            if currQueue.right:
                queue.append(currQueue.right)

        return root

        
        