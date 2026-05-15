# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from collections import deque

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        q = deque()
        res = False
        if root:
            q.append(root)
        while (q and not res) == True:
            currQ = q.popleft()
            if currQ.val == subRoot.val:
                res = self.checkIsSame(currQ,subRoot)
                print(res)
            
            if currQ.left:
                q.append(currQ.left)
            if currQ.right:
                q.append(currQ.right)

        return res
    
    def checkIsSame(self, root2:Optional[TreeNode],subRoot2:Optional[TreeNode])->bool:
            queues = deque()
            res2 = True
            if root and subRoot:
                queues.append((root2,subRoot2))
            while queues and res2:
                currRoot,currSubRoot = queues.popleft()
                
                if currRoot.val != currSubRoot.val:
                    res2 = False
                    break


                if currRoot.left and currSubRoot.left:
                    queues.append((currRoot.left,currSubRoot.left))
                if currRoot.right and currSubRoot.right:
                    queues.append((currRoot.right,currSubRoot.right))
                
                if (currRoot.left or currSubRoot.left)and not (currRoot.left and currSubRoot.left):
                    res2 = False 
                    break
                if (currRoot.right or currSubRoot.right) and not (currRoot.right and currSubRoot.right):
                    res2 = False
                    break
                    

                

            return res2
    