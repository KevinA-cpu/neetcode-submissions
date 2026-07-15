# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        result = {'value': 0}

        def rec(root, count, result):
            if root is None:
                return

            if count > result['value']:
                result['value'] = count
            
            rec(root.left, count+1, result)
            rec(root.right, count+1, result)

        rec(root, 1, result)
        return result['value']