from collections import deque
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        
        s=deque([root])
        ans=[]

        while s:
            levelsize=len(s)
            curr=[]
            for i in range(levelsize):
                temp = s.popleft()
                curr.append(temp.val)

                if temp.left:
                    s.append(temp.left)
                if temp.right:
                    s.append(temp.right)

            ans.append(curr)


        return ans
        

        
        