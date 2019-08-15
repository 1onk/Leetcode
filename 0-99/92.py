# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def reverseBetween(self, head: ListNode, m: int, n: int) -> ListNode:
        if not head:
            return None

        cur, prev = head, None
        while m > 1:
            prev = cur
            cur = cur.next
            m -= 1
            n -= 1

        tail, con = cur, prev
        while n:
            third = cur.next
            cur.next = prev
            prev = cur
            cur = third
            n -= 1

        if con:
            con.next = prev
        else:
            head = prev
        tail.next = cur
        return head


