# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        
        # iterative
        stack = [(root, False)]
        ans = []
        while stack:
            curr, visited = stack.pop()
            if curr:
                if visited:
                    ans.append(curr.val)
                else:
                    stack.append((curr, True))
                    stack.append((curr.right, False))
                    stack.append((curr.left, False))

                    
        return ans
        
        
        '''
        # recursive
        def dfs(root, ans):
            if not root:
                return None
            dfs(root.left, ans)
            dfs(root.right, ans)
            ans.append(root.val)
            
        ans = []
        dfs(root, ans)
        return ans
        '''
