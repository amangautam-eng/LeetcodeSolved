# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: TreeNode | None, k: int) -> int:
        arr=[]
        def toarray(root):
            if root:
                toarray(root.left)
                arr.append(root.val)
                toarray(root.right)
        toarray(root)
        sort=sorted(arr)
        return sort[k-1]


        