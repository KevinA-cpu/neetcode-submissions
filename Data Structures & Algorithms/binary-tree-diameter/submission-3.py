# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        if root is None:
            return 0
        mapper = {'val':0}

        def findMax(root):
            if root is None:
                return 0
            
            leftMax = findMax(root.left)
            rightMax = findMax(root.right)
            print(root.val, leftMax, rightMax)

            current = max(leftMax + rightMax, max(leftMax, rightMax) + 1)
            if current > mapper['val']:
                mapper['val'] = current

            return max(leftMax, rightMax) + 1


        leftMax = findMax(root.left)
        rightMax = findMax(root.right)
        current = max(leftMax + rightMax, max(leftMax, rightMax))
        if current > mapper['val']:
            mapper['val'] = current

        return mapper['val']
            
        