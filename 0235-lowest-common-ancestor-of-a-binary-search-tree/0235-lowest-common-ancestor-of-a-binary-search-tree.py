# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':

        def search(root):
            if root is None:
                return 
            if root==p or root==q:
                return root
            

            left=search(root.left)
            right=search(root.right)

            if left is not None and right is not None:
                return root
            if left is None:
                return right
            if right is None:
                return left

        return search(root)

            

            

            
        