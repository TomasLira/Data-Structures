class linked_list():
    def __init__(self,value):
        self.value = value
        self.next = None

    def insert_node(self,node):
        tmp = self
        head = self
        while tmp.next is not None:
            tmp = tmp.next
        tmp.next = node
        return head

    def delete_value(self,target_value):
        head = self
        while head is not None:
            if head.value == target_value:
                tmp = head.next
                head.next = None
                head = tmp
            else:
                break

        if head is not None:
            prev_node = None
            current_node = head
            while current_node is not None:
                if current_node.value != target_value:
                    prev_node = current_node
                    current_node = current_node.next
                else:
                    prev_node.next = current_node.next
                    current_node.next = None
                    current_node = prev_node.next
        return head
          
head = linked_list(10)

node1 = linked_list(11)
node2 = linked_list(12)
node3 = linked_list(14)
node4 = linked_list(14)

head = head.insert_node(node1)
head = head.insert_node(node2)
head = head.insert_node(node3)
head = head.insert_node(node4)

head = head.delete_value(14)

while head is not None:
    print(head.value)
    head = head.next

