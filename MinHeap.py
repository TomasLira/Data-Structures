class Minheap():
    def __init__(self):
        self.heap = []
    def insert_value(self,new_value):
        self.heap.append(new_value)
        self.sift_up()

    def sift_up(self):
        current_index = len(self.heap) -1
        parent_index = (current_index-1)//2
        while current_index > 0:
            if self.heap[current_index] < self.heap[parent_index]:
                self.heap[current_index],self.heap[parent_index] = self.heap[parent_index],self.heap[current_index]
            current_index =  parent_index
            parent_index = (current_index-1)//2

    def remove_min_value(self):
        self.heap[-1],self.heap[0] = self.heap[0],self.heap[-1]
        self.heap.pop()
        self.sift_down()


    def sift_down(self):
        current_index = 0
        child_one = 1
        child_two = 2
        while child_one < len(self.heap):
            if  child_two < len(self.heap):
                if self.heap[child_one] > self.heap[child_two]:
                    new_idx = child_two
                else:
                    new_idx = child_one
            else:
                new_idx = child_one

            if self.heap[new_idx] < self.heap[current_index]:
                self.heap[new_idx],self.heap[current_index] = self.heap[current_index],self.heap[new_idx]
                current_index = new_idx
                child_one = current_index*2 + 1
                child_two = current_index*2 + 2
            else:
                return 

    def peek_min_value(self):
        print(self.heap)
 
Heap = Minheap()
Heap.insert_value(10)
Heap.insert_value(100)
Heap.insert_value(78)
Heap.insert_value(76)
Heap.insert_value(23)
Heap.insert_value(17)
Heap.insert_value(89)
Heap.insert_value(1)
Heap.remove_min_value()
Heap.peek_min_value()


#               10
##             /  \
#            100   78
#            / \   / \
#          76 23   17 89      
#
#
#
#
#