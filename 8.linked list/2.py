# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        def convertToNumber(node):
            number = ''
            while node:
                number = str(node.val) + number
                node = node.next
            return int(number)
        
        def convertToList(array):
            node = None
            while array:
                val = int(array.pop())
                if not node:
                    node = ListNode(val)
                    head = node
                else:
                    head.next = ListNode(val)
                    head = head.next
            return node
        
        number = convertToNumber(l1) + convertToNumber(l2)
        array = list(str(number))
        
        return convertToList(array)