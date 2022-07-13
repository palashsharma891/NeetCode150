# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
#         def reverseUtil(head):
#             curr, prev = head, None
#             while curr:
#                 temp = curr.next
#                 curr.next = prev
#                 prev = curr
#                 curr = temp
#             return head
        
#         list1 = reverseUtil(l1)
#         list2 = reverseUtil(l2)
        
        r = 1
        num1 = 0
        while l1:
            num1 += l1.val * r
            r *= 10
            l1 = l1.next
        
        r = 1
        num2 = 0
        while l2:
            num2 += l2.val * r
            r *= 10
            l2 = l2.next
        
        dummy = node = ListNode()
        s = num1 + num2
        
        while s > 0:
            r = s % 10
            node.val = r
            s = s // 10
            if s > 0: # add a node only if digits are left in s, otherwise create special case for s = 0 before while loop
                node.next = ListNode()
                node = node.next
            
        return dummy
