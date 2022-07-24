# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        
        # iterative
        if not root:
            return 0
        
        q = [root]
        levels = 0
        
        while q:
            l = len(q)
            for i in range(l):
                curr = q.pop(0)
                if curr.left:
                    q.append(curr.left)
                if curr.right:
                    q.append(curr.right)
            
            levels += 1
                
        return levels
        
        '''
        #recursive
        if not root:
            return 0
        
        l = 1 + self.maxDepth(root.left)
        r = 1 + self.maxDepth(root.right)
        
        return max(l, r)
        '''
