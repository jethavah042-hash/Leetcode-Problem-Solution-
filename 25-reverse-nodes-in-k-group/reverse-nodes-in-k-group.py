# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution(object):
    def reverseKGroup(self, head, k):
        if not head or k == 1:
            return head
        
        dummy = ListNode(0)
        dummy.next = head
        prev_group = dummy
        
        while True:
            kth = prev_group
            for i in range(k):
                kth = kth.next
                if not kth:
                    return dummy.next
            
            group_next = kth.next
            prev = group_next
            curr = prev_group.next
            
            for i in range(k):
                temp = curr.next
                curr.next = prev
                prev = curr
                curr = temp
            
            temp = prev_group.next
            prev_group.next = prev
            prev_group = temp