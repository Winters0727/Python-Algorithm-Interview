class MyCircularQueue:

    def __init__(self, k: int):
        self.length = k
        self.data = []
        self.empty = True
        self.full = False

    def enQueue(self, value: int) -> bool:
        if self.full:
            return False
        
        self.data.append(value)
        
        if self.empty:
            self.empty = False
        
        if len(self.data) == self.length:
            self.full = True
            
        return True

    def deQueue(self) -> bool:
        if self.empty:
            return False
        
        self.data.pop(0)
        
        if self.full:
            self.full = False
            
        if len(self.data) == 0:
            self.empty = True
            
        return True
    
    def Front(self) -> int:
        if self.empty:
            return -1
        return self.data[0]

    def Rear(self) -> int:
        if self.empty:
            return -1
        return self.data[-1]

    def isEmpty(self) -> bool:
        if self.empty:
            return True
        return False

    def isFull(self) -> bool:
        if self.full:
            return True
        return False


# Your MyCircularQueue object will be instantiated and called as such:
# obj = MyCircularQueue(k)
# param_1 = obj.enQueue(value)
# param_2 = obj.deQueue()
# param_3 = obj.Front()
# param_4 = obj.Rear()
# param_5 = obj.isEmpty()
# param_6 = obj.isFull()