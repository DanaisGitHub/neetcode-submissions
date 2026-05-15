# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        # underlying the deepest and most right nodes show,
        # 

        res=[]

        def dfs(rootNode:Optional[TreeNode],depth:int):
            if not rootNode:
                return None
            
            if depth == len(res): 
                res.append(rootNode.val)

            dfs(rootNode.right,depth+1)
            dfs(rootNode.left,depth+1)
            
        dfs(root,0)
        return res

        
        