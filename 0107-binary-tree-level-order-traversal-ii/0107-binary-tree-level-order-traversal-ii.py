# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrderBottom(self, root: Optional[TreeNode]) -> List[List[int]]:

        if root==None:
            return []

        if root.left==None and root.right==None:
            return [[root.val]]

        s=deque([root])
        ans=deque()

        while s :
            levels=len(s)
            temp=[]
            for i in range(levels):
                curr=s.popleft()
                temp.append(curr.val)

                if curr.left:
                    s.append(curr.left)
                if curr.right:
                    s.append(curr.right)

            ans.appendleft(temp)
        
        return list(ans)

        