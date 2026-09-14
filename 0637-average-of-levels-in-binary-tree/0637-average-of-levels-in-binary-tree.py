# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def averageOfLevels(self, root: Optional[TreeNode]) -> List[float]:

        if root is None:
            return 0

        if root.left==None and root.right==None:
            return [root.val]
            
        s=deque([root])
        ans=[]

        while s:
            level=len(s)
            temp=[]
            for i in range(level):
                curr=s.popleft()

                temp.append(curr.val)

                if curr.left:
                    s.append(curr.left)
                if curr.right:
                    s.append(curr.right)

            ans.append(sum(temp)/len(temp))

        return ans


        