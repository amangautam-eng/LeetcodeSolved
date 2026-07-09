from collections import deque
from typing import Optional, List

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    # 1. Added 'self' parameter
    def preorder(self, node: Optional[TreeNode]) -> List[int]:
        # 2. Handled the empty tree edge case
        if not node:
            return []
            
        stack = deque([node])
        ans = []
        
        while stack:
            curr = stack.pop()
            ans.append(curr.val)
            
            # Right child is pushed first so Left is processed first (LIFO)
            if curr.right:
                stack.append(curr.right)
            # 3. Fixed 'current.left' typo to 'curr.left'
            if curr.left:
                stack.append(curr.left)
                
        return ans

    def searchBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        while root:
            if root.val == val:
                return root
            elif root.val > val:
                root = root.left
            else:
                root = root.right
        return None
