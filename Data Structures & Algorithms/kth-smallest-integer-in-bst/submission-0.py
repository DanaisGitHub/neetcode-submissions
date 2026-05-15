# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        # possible ways to solve
        # in order then reverse

        return (self.reverseInOrder(root))[-k]

    
    def reverseInOrder(self,root:Optional[TreeNode]) -> List[int]:
        if not root:
            return[]
        
        return self.reverseInOrder(root.right) + [root.val] + self.reverseInOrder(root.left)

        