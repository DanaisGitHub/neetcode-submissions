# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        # solve  interative stack style

        stack = [[p,q]]
        if not p and not q:
            return True
        if not p or not q:
            return False

        while stack:
            np,nq = stack.pop()
            if np.val != nq.val:
                print("val = false")
                return False
            
            if np.left and nq.left:
                stack.append([np.left,nq.left])
                continue
            if np.left or nq.left:
                print("left struct = false")
                return False

            if np.right and nq.right:
                stack.append([np.right,nq.right])
                continue
            if np.right or nq.right:
                print("right struct = false")
                return False

            
        return True
        
