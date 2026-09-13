# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        self.total=0

        notes=[]
        def sumnode(root):
            notes.append(str(root.val))

            if root.left==None and root.right==None:
                self.total += int("".join(notes))
            else:
                if root.left:
                    sumnode(root.left)
                if root.right:
                    sumnode(root.right)


            notes.pop()


        sumnode(root)
        return self.total
            


            


        