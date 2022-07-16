# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        
        dummy = ListNode(0, head)
        groupPrev = dummy
        
        while True:
            kth = self.getkth(groupPrev, k)
            if not kth: #if less than k nodes are remaining in the list
                break
            groupNext = kth.next
            
            #reverse group
            prev, curr = kth.next, groupPrev.next
            while curr != groupNext:
                temp = curr.next
                curr.next =prev
                prev = curr
                curr = temp

            tmp = groupPrev.next
            groupPrev.next = kth
            groupPrev = tmp
        
        return dummy.next

    def getkth(self, curr, k):
        while curr and k:
            curr = curr.next
            k -= 1
        return curr
        
