# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        
        def rec(p, q):
            if (p is not None and q is None) or (p is None and q is not None):
                return False
            
            if (p is None and q is None):
                return True


            return p.val==q.val and rec(p.left, q.left) and rec(p.right, q.right)
        
        return rec(p,q)