# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        # I STILL DON'T UNDERSTAND THE QUESTION

        
        # the height of the left + height of right 

        if not root:
            return 0
        
        left = self.branchHeight(root.left)
        right = self.branchHeight(root.right)

        

        return max (left + right, self.diameterOfBinaryTree(root.right),self.diameterOfBinaryTree(root.left))

    def branchHeight(self, root: Optional[TreeNode])->int:
        if not root:
            return 0

        return 1 + max(self.branchHeight(root.right),
        self.branchHeight(root.left))

        

        