class Node:
    def __init__(self, value=None):
        self.value = value
        self.next = None

class LinkedList:
    def __init__(self, array=None):
        self.head = None
        if array:
            for value in array:
                if not self.head:
                    self.head = Node(value)
                    head = self.head
                else:
                    head.next = Node(value)
                    head = head.next

    def __len__(self):
        if not self.head:
            return 0
        length = 1
        head = self.head
        while head.next:
            head = head.next
            length += 1
        return length

    def __str__(self):
        if self.empty():
            return '[]'
        result = '['
        head = self.head
        while head:
            result += f'{str(head.value)} '
            head = head.next
        result = result[:-1] + ']'
        return result

    def empty(self):
        if self.head:
            return False
        return True
    
    def insert(self, value):
        if self.empty():
            self.head = Node(value)
            return self.head

        head = self.head
        
        while head.next:
            head = head.next
        head.next = Node(value)
        
        return head.next.value

    def pop(self):
        if self.empty():
            raise Exception('LinkedList is empty!')
        head = self.head
        if not head.next:
            return head

        while head.next.next:
            head = head.next

        result = head.next.value
        head.next = None

        return result

    def find(self, value):
        if self.empty():
            raise Exception('LinkedList is empty!')
        head = self.head
        while head:
            if head.value == value:
                return True
            head = head.next
        return False

    def tail(self):
        if self.empty():
            return None

        head = self.head
        
        while head.next:
            head = head.next
        
        return head.value