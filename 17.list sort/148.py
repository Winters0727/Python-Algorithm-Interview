# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def sortList(self, head: ListNode) -> ListNode:
        if not head or not head.next:
            return head
        
        values = []
        node_head = head
        while node_head != None:
            values.append(node_head.val)
            node_head = node_head.next
        values.sort(reverse=True)
        
        answer = answer_head = ListNode(values.pop())
        while values:
            answer_head.next = ListNode(values.pop())
            answer_head = answer_head.next
        return answer