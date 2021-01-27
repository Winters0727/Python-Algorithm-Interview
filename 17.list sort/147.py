# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def insertionSortList(self, head: ListNode) -> ListNode:
        if not head or not head.next:
            return head
        
        answer_head = None
        while head:
            if answer_head == None:
                answer = answer_head = ListNode(head.val)
                head = head.next
            else:
                rear_node = answer_head
                while answer_head:
                    if answer_head.val > head.val and answer == answer_head:
                        answer = ListNode(head.val)
                        answer.next = answer_head
                        break
                    elif answer_head.val > head.val and answer != answer_head:
                        rear_node.next = ListNode(head.val)
                        rear_node.next.next = answer_head
                        break
                    else:
                        rear_node = answer_head
                        answer_head = answer_head.next
                else:
                    rear_node.next = ListNode(head.val)
                answer_head = answer
                head = head.next
        return answer