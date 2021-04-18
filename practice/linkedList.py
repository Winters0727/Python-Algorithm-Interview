class LinkedList:
    def __init__(self, head=None):
        self.head = head

class Node:
    def __init__(self, value=None):
        self.value = value
        self.next = None

linked_list = LinkedList()

for num in range(1,10001):
    node = Node(num)
    if not linked_list.head:
        linked_list.head = node
        now = linked_list.head
    else:
        now.next = node
        now = node

head = linked_list.head
while head.next:
    print(head.value)
    head = head.next
else:
    print(head.value)