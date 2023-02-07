class binary_search_tree():
    def __init__(self,value):
        self.value = value
        self.right = None
        self.left =  None
        self.parent = None

    def find_node(self,target_value):
        current_node = self 
        if current_node is None:
            return None
        if current_node.value != target_value and current_node.right is None and current_node.left is None:
            return False

        if current_node.value == target_value:
            return current_node  
        elif current_node.value < target_value and current_node.right is not None: 
            return current_node.right.find_node(target_value)
        elif current_node.value > target_value and current_node.left is not None:
            return current_node.left.find_node(target_value)

        
    def insert_node(self,new_value):
        current_node = self
        if current_node is None:
            new_node = binary_search_tree(new_value)
            return 
        if current_node.value < new_value:
            if current_node.right is None:
                new_node = binary_search_tree(new_value)
                new_node.parent = current_node
                current_node.right = new_node
            else:
                current_node.right.insert_node(new_value)

        elif  current_node.value > new_value:
            if current_node.left is None:
                new_node = binary_search_tree(new_value)
                new_node.parent = current_node
                current_node.left = new_node
            else:
                current_node.left.insert_node(new_value)

    def remove_node(self,node):
        if node is None:
            return None

        if node.right is None and node.left is None:
            parent_node = node.parent
            if parent_node is not None:
    
                if parent_node.right is node:
                    parent_node.right = None
                    node.parent = None
                elif parent_node.left is node:
                    parent_node.left = None
                    node.parent = None

        if node.right is None or node.left is None:
            parent_node = node.parent
            if parent_node is not None:
                if node.left is not None:
                    child_node = node.left
                    node.left = None
                    if parent_node.right is node:
                        parent_node.right = child_node
                    else:
                        parent_node.left = child_node
                else:
                    child_node = node.right
                    node.right = None
                    if parent_node.right is node:
                        parent_node.right = child_node
                    else:
                        parent_node.left = child_node
                node.parent = None
        
        if node.left is not None and node.right is not None:

            successor_node = node.right
            while successor_node.left is not None:
                successor_node = successor_node.left
            self.remove_node(successor_node)
            parent_node = node.parent
            
            if parent_node is None:
                node.value = successor_node.value
            if parent_node is not None:
                if parent_node.left is node:
                    parent_node.left = successor_node
                else:
                    parent_node.right = successor_node
            successor_node.parent = node.parent
            successor_node.left = node.left
            node.left.parent = successor_node
            successor_node.right = node.right
            if node.right is not None:
                node.right.parent = successor_node
            
             
def print_nodes_values(node):
    print(node.value)
    if node.left is not None:
        print_nodes_values(node.left)
    if node.right is not None:
        print_nodes_values(node.right)

root = binary_search_tree(10)
root.insert_node(15)
root.insert_node(13)
root.insert_node(21)
root.insert_node(20)
root.insert_node(22)
root.insert_node(5)
root.insert_node(8)
root.insert_node(3)
root.remove_node(root.find_node(10))

print_nodes_values(root)
