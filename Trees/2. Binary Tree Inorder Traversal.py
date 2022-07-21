# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        
        # iterative 1
        stack = [(root, False)]
        ans = []
        while stack:
            curr, visited = stack.pop()
            if curr:
                if visited:
                    ans.append(curr.val)
                else:
                    stack.append((curr.right, False))
                    stack.append((curr, True))
                    stack.append((curr.left, False))
                    
        return ans
        
        
        '''
        # iterative 2
        if not root:
            return None
        
        stack = []
        ans = []
        while True:
            while root:
                stack += [root]
                root = root.left
            if not stack:
                return ans
            curr = stack.pop()
            ans += [curr.val]
            root = curr.right
        
        return ans
        '''            
        
        '''
        # recursive
        def dfs(root, ans):
            if not root:
                return None
            dfs(root.left, ans)
            ans += [root.val]
            dfs(root.right, ans)
            
        ans = []
        dfs(root, ans)
        return ans
        '''
