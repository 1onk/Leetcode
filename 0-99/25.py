# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def reverseKGroup(self, head: ListNode, k: int) -> ListNode:


        def reverse(head):
            pre = None
            curr = head
            while curr:
                next = curr.next
                curr.next = pre
                pre = curr
                curr = next
            return pre


        dummy = ListNode(0)
        dummy.next = head

        pre = dummy
        end = dummy



        while end.next:
            for i in range(k):
                if not end:
                    break
                end = end.next

            if not end:
                break

            start = pre.next
            next = end.next
            end.next = None
            pre.next = reverse(start)
            start.next = next
            pre = start
            end = pre

        return dummy.next

