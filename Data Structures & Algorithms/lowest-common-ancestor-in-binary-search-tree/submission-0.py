# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        # for each node can you find p and q
        # if either going left or right stops this that node is the LCA
        # if you could of found p or q in left or right branches
        # when you can only find 1 or none previous node is 

        # you have the right idea, you may need to think about it from more a DFS perspective

        # from each node we can find p and q in left or right or left or right or self right or self left
        # if self, the is lca, if left and right lca
        # from there we need to move differently

        pFoundR = self.__findX(root.right,p)
        qFoundR = self.__findX(root.right,q)
        if qFoundR and pFoundR:
            return self.lowestCommonAncestor(root.right,p,q)

        pFoundL = self.__findX(root.left,p)
        qFoundL = self.__findX(root.left,q)
        if qFoundL and pFoundL:
            return self.lowestCommonAncestor(root.left,p,q)


        if pFoundL and qFoundR or pFoundR and qFoundL or (root.val == p.val and qFoundL or qFoundR) or (root.val == q.val and pFoundL or pFoundR)  :
            return root






    def __findX(self,root: TreeNode,x: TreeNode) -> bool:

        if not root:
            return False

        if root.val == x.val:
            return True
        
        return False or self.__findX(root.right,x) or self.__findX(root.left,x)

   
        

    
        