"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: 'Node') -> 'Node':
        nodeMap = {}
        visited = set()
        
        def dfs(node):
            if node in nodeMap:
                return nodeMap[node]
            
            nodeCopy = Node(node.val)
            nodeMap[node] = nodeCopy
            for nei in node.neighbors:
                temp = dfs(nei)
                nodeCopy.neighbors.append(temp)
            
            return nodeCopy
        
        return dfs(node) if node else None
