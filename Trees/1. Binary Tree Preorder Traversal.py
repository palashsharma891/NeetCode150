# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        
        # iterative
        
        if not root:
            return None
        
        stack = [root]
        ans = []
        while stack:
            curr = stack.pop()
            ans += [curr.val]
            if curr.right:
                stack += [curr.right]
            if curr.left:
                stack += [curr.left]
            print(ans)
                
        return ans
        
        '''
        # recursive
        def dfs(root, ans):
            if not root:
                return None
            
            ans += [root.val]
            dfs(root.left, ans)
            dfs(root.right, ans)
            
        ans = []
        dfs(root, ans)
        return ans
        '''
