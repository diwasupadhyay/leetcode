# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None:
            return None
        odd_current = head
        even_head = head.next
        even_current = head.next
      
        while even_current and even_current.next:
            odd_current.next = even_current.next
            odd_current = odd_current.next
            even_current.next = odd_current.next
            even_current = even_current.next
    
        odd_current.next = even_head
      
        return head