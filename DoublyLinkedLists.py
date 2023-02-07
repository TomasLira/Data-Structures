class doubly_linked_list():
    def __init__(self,value):
        self.value = value
        self.next = None
        self.prev = None
    
    def insert_node(self,node,tail):
        current_node = self
        head = self
        while current_node.next is not None:
            current_node = current_node.next
        current_node.next = node
        node.prev = current_node
        tail = node
        return head,tail
    
    def delete_value(self,target_value,tail):
        head = self
        while head is not None:
            if head.value != target_value:
                break
            else:
                tmp = head.next
                if tmp is not None:
                    tmp.prev = None
                    head.next = None
                    head = tmp
                else:
                    return None,None
        current_node = head
        prev_node = None

        while current_node is not None:
            if current_node.value != target_value:
                prev_node = current_node
                current_node = current_node.next
            else:
                tmp = current_node.next
                prev_node.next = tmp
                current_node.prev = None
                current_node.next = None
                if tmp is not None:
                    tmp.prev = prev_node
                current_node = prev_node.next
        
        tmp = head
        while tmp.next is not None:
            tmp = tmp.next
        tail = tmp
        return head,tail
        
    def length(self):
        counter = 0
        tmp = self
        while tmp is not None:
            counter += 1
            tmp = tmp.next
        return counter
        
    # O(nˆ2) time | O(1) space
    def sort_linked_list(self):
        current_node = self
        while current_node.next is not None:
            tmp_node = current_node.next
            node = current_node
            while tmp_node is not None:
                if tmp_node.value < node.value:
                    node.value,tmp_node.value = tmp_node.value,node.value
                tmp_node = tmp_node.next
                node = node.next
            current_node = current_node.next


head = doubly_linked_list(20)
tail = head 

node1 = doubly_linked_list(28)
node2 = doubly_linked_list(22)
node3 = doubly_linked_list(21)
node4 = doubly_linked_list(40)


head,tail = head.insert_node(node1,tail)
head,tail = head.insert_node(node2,tail)
head,tail = head.insert_node(node3,tail)
head,tail = head.insert_node(node4,tail)

print("the length of the linked list is: {}".format(head.length())),print()
head.sort_linked_list()
head,tail= head.delete_value(24,tail)

tmp = head
while tmp is not None:
    print(tmp.value)
    tmp = tmp.next

print()
tmp = tail

while tmp is not None:
    print(tmp.value)
    tmp = tmp.prev