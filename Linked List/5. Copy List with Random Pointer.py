"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        
        copy = {None:None}
        
        curr = head
        
        while curr:
            node = Node(curr.val)
            copy[curr] = node
            curr = curr.next
            
        curr = head
        
        while curr:
            node = copy[curr]
            node.next = copy[curr.next]
            node.random = copy[curr.random]
            curr = curr.next
            
        return copy[head]
