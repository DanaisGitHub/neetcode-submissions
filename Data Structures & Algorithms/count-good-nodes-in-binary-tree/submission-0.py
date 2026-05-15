# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        goodNodesRet = 0

        def dfs(rootNode,pathMax):
            if not rootNode:
                return 
            
            if rootNode.val >= pathMax:
                nonlocal goodNodesRet
                goodNodesRet += 1
                pathMax = max(pathMax,rootNode.val)
            dfs(rootNode.right,pathMax)
            dfs(rootNode.left,pathMax)
            
        
        dfs(root,root.val)
        return goodNodesRet
        



        
            
            
        