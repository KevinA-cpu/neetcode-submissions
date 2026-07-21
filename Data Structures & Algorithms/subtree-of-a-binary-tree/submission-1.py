# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if root is None and subRoot is not None: 
            return False
        
        if subRoot is None and root is not None:
            return False
        
        if root is None and subRoot == root:
            return True

        def rec(root, subRoot):
            if root is None and subRoot is not None: 
                return False
            
            if subRoot is None and root is not None:
                return False
            
            if root is None and subRoot == root:
                return True

            return root.val == subRoot.val and rec(root.left, subRoot.left) and rec(root.right, subRoot.right) 

        stack = [root]
        while(stack):
            cur = stack.pop()

            if cur.val == subRoot.val:
                if rec(cur,subRoot):
                    return True
            
            if cur.left is not None:
                stack.append(cur.left)
            if cur.right is not None:
                stack.append(cur.right)

        return False



            
