# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        values = []
        current = head
        while current:
            values.append(current.val)
            current = current.next
        n = len(values)
        max_twin_sum = max(values[i] + values[n - 1 - i] for i in range(n // 2))
        return max_twin_sum