# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:

    def hasPathSum(self, root: Optional[TreeNode], target: int) -> bool:
        if(root==None): 
            return False
        target=target-root.val

        if(root.left==None and root.right==None):
            if(target==0): 
                return True
            else: 
                return False
        
        left=self.hasPathSum(root.left,target)
        if(left):
            return True

        right=self.hasPathSum(root.right,target)
        if(right):
            return True

        return False

