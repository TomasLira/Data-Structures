class node():
    def __init__(self,value):
        self.value = value
        self.next = None
    
class stack():
    def __init__(self):
        self.head = None

    def is_empty(self):
        if self.head is None:
            return True
        else:
            return False

    def peek(self):
        print(self.head.value)

    def push(self,value):
        if self.head is None:
            self.head = node(value)
        else:
            current_node = node(value)
            current_node.next = self.head
            self.head = current_node
            
    def pop(self):
        if self.is_empty():
            return False
        head_value = self.head.value
        tmp = self.head
        self.head = self.head.next
        tmp.next = None
        return head_value


Stack = stack()
Stack.push(11)
Stack.push(12)
Stack.push(13)
Stack.push(14)
Stack.peek()
print()
print(Stack.pop())
print(Stack.pop())
print(Stack.pop())
print(Stack.pop())
print(Stack.pop())
        




    