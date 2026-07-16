# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        result = {'val':True}
        def rec(root, result):
            if root is None:
                return 0
            
            left = rec(root.left, result)
            right = rec(root.right, result)

            if abs(left-right) > 1:
               result['val'] = False

            return max(left, right) + 1

        rec(root, result)
        return result['val']
        