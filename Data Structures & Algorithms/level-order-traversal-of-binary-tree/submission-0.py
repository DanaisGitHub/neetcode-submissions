# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        levelOrderRes = []

        def dfs(rootNode:Optional[TreeNode],depth:int): # purpose is to alter 
            if not rootNode:
                return None
            if len(levelOrderRes) == depth:
                levelOrderRes.append([])
            levelOrderRes[depth].append(rootNode.val)
            dfs(rootNode.left,depth+1)
            dfs(rootNode.right,depth+1)

        dfs(root,0)
        return levelOrderRes
        

            
        
            


