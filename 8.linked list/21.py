# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        def takeAllValue(node):
            array = []
            while node:
                array.append(node.val)
                node = node.next
            return array
        
        def convert(array):
            nodes = ListNode(array.pop())
            while array:
                node = ListNode(array.pop())
                if nodes.next == None:
                    nodes.next = node
                else:
                    rear_node.next = node
                rear_node = node
            return nodes
                
            
        if not l1 and not l2:
            return l1
        elif not l1:
            return convert(takeAllValue(l2)[::-1])
        elif not l2:
            return convert(takeAllValue(l1)[::-1])
        else:
            result = []
            while l1 and l2:
                if l1.val <= l2.val:
                    result.append(l1.val)
                    l1 = l1.next
                else:
                    result.append(l2.val)
                    l2 = l2.next

            if l1:
                result.extend(sorted(takeAllValue(l1)))
            else:
                result.extend(sorted(takeAllValue(l2)))
                  
            return convert(result[::-1])