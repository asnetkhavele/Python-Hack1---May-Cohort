class QueueWithStacks:
    def __init__(self):
        self.stack1 = []
        self.stack2 = []
    
    def enqueue(self, x: int):
        self.stack1.append(x)
    
    def dequeue(self) -> int:
        if not self.stack2:
            while self.stack1:
                self.stack2.append(self.stack1.pop())
        
        if not self.stack2:
            raise IndexError("Dequeue from an empty queue")
        
        return self.stack2.pop()

if __name__ == "__main__":
    q = QueueWithStacks()
    q.enqueue(1)
    q.enqueue(2)
    print(q.dequeue())  # Output: 1
    print(q.dequeue())  # Output: 2