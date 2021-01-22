# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: ListNode) -> bool:
        if not head:
            return True
        
        result = []
        result.append(head.val)
        next_head = head.next
        while next_head:
            result.append(next_head.val)
            next_head = next_head.next
        return result == result[::-1]