# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        # bst = left -> smaller, right -> bigger
        # nodes left->right = smaller -> bigger
        
        # in order traversal, end array should be in order
        inOrderTree = self.inOrder(root)

        return all(inOrderTree[i] < inOrderTree[i+1] for i in range (len(inOrderTree)-1))



    
    def inOrder(self,root:Optional[TreeNode]) -> List[int]:
        if not root:
            return []
        
        return self.inOrder(root.left) + [root.val]+ self.inOrder(root.right) 

        