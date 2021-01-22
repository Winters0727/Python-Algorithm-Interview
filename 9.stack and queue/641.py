class MyCircularDeque:

    def __init__(self, k: int):
        """
        Initialize your data structure here. Set the size of the deque to be k.
        """
        self.length = k
        self.data = []
        self.empty = True
        self.full = False
        

    def insertFront(self, value: int) -> bool:
        """
        Adds an item at the front of Deque. Return true if the operation is successful.
        """
        if self.full:
            return False
        
        self.data = [value] + self.data
        
        if self.empty:
            self.empty = False
        
        if len(self.data) == self.length:
            self.full = True
            
        return True

    def insertLast(self, value: int) -> bool:
        """
        Adds an item at the rear of Deque. Return true if the operation is successful.
        """
        if self.full:
            return False
        
        self.data.append(value)
        
        if self.empty:
            self.empty = False
        
        if len(self.data) == self.length:
            self.full = True
            
        return True

    def deleteFront(self) -> bool:
        """
        Deletes an item from the front of Deque. Return true if the operation is successful.
        """
        if self.empty:
            return False
        
        self.data.pop(0)
        
        if self.full:
            self.full = False
            
        if len(self.data) == 0:
            self.empty = True
            
        return True

    def deleteLast(self) -> bool:
        """
        Deletes an item from the rear of Deque. Return true if the operation is successful.
        """
        if self.empty:
            return False
        
        self.data.pop()
        
        if self.full:
            self.full = False
            
        if len(self.data) == 0:
            self.empty = True
            
        return True

    def getFront(self) -> int:
        """
        Get the front item from the deque.
        """
        if self.empty:
            return -1
        return self.data[0]

    def getRear(self) -> int:
        """
        Get the last item from the deque.
        """
        if self.empty:
            return -1
        return self.data[-1]

    def isEmpty(self) -> bool:
        """
        Checks whether the circular deque is empty or not.
        """
        if self.empty:
            return True
        return False

    def isFull(self) -> bool:
        """
        Checks whether the circular deque is full or not.
        """
        if self.full:
            return True
        return False


# Your MyCircularDeque object will be instantiated and called as such:
# obj = MyCircularDeque(k)
# param_1 = obj.insertFront(value)
# param_2 = obj.insertLast(value)
# param_3 = obj.deleteFront()
# param_4 = obj.deleteLast()
# param_5 = obj.getFront()
# param_6 = obj.getRear()
# param_7 = obj.isEmpty()
# param_8 = obj.isFull()