# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if root == None:
            return root
        
        queue = deque([root])

        while queue:
            node = queue.popleft()

            node.left,node.right = node.right,node.left

            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
        
        return root















        
        if not root: # if empty
            return None

        queue = deque([root]) # top of tree on queue
        while queue:# while there's stuff in the queue
            node = queue.popleft() # take the 1st element put in


            node.left, node.right = node.right, node.left # concurrent i think


            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
        return root