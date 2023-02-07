class node():
    def __init__(self,value):
        self.value = value
        self.next = None

class queue():
    def __init__(self):
        self.front = None
        self.back = None
    def is_empty(self):
        if self.back is None:
            return True
        else:
            return False
    def enqueue(self,value):
        if self.is_empty():
            self.front = node(value)
            self.back = self.front
        else:
            current_node = node(value)
            self.back.next = current_node
            self.back = current_node
    def dequeue(self):
        if self.is_empty():
            return False
        if self.front == self.back:
            front_value = self.front.value
            self.front = None
            self.back = None
            return front_value
        else:
            front_value = self.front.value 
            tmp_node = self.front
            self.front = self.front.next
            tmp_node.next = None
            return front_value

        
Queue = queue()
Queue.enqueue(10)
Queue.enqueue(11)
Queue.enqueue(12)
Queue.enqueue(13)
Queue.enqueue(14)

print(Queue.dequeue())
print(Queue.dequeue())
print(Queue.dequeue())
print(Queue.dequeue())
print(Queue.dequeue())
print(Queue.dequeue())





