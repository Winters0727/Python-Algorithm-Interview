# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
import heapq

class Solution:
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        answer = head = ListNode(None)
        heap = []
        
        for index in range(len(lists)):
            if lists[index]:
                heapq.heappush(heap,(lists[index].val, index, lists[index]))
                
        while heap:
            node = heapq.heappop(heap)
            index = node[1]
            min_node = node[2]
            head.next = min_node
            
            head = head.next
            
            if min_node.next:
                heapq.heappush(heap, (min_node.next.val, index, min_node.next))
            
        return answer.next 