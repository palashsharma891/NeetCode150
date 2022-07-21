# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        
        # DFS recursive
        def dfs(root, level, ans):
            if not root:
                return
            if len(ans) < level+1:
                ans.append([])
            ans[level].append(root.val)
            dfs(root.left, level+1, ans)
            dfs(root.right, level+1, ans)
            
        ans = []
        level = 0
        dfs(root, level, ans)
        return ans
        
        
        '''
        # BFS iterative
        if not root:
            return None
        
        q = [root]
        res = []
        
        while q:
            row = []
            l = len(q)
            for i in range(l):
                curr = q.pop(0)
                row.append(curr.val)
                if curr.left:
                    q.append(curr.left)
                if curr.right:
                    q.append(curr.right)
            res.append(row)
                
        return res
        '''
