# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
from collections import deque
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        link = head

        l = []
        while link:
            l.append(link.val)
            link = link.next

        d = deque(l)
        d.rotate(k)
        d = list(d)[::-1]
        ans = None
        for x in d:
            temp = ListNode(x)
            temp.next = ans
            ans = temp
        return ans
