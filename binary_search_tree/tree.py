class TreeNode:
    def __init__(self, key, val=None):
        if val == None:
            val = key

        self.key = key
        self.value = val
        self.left = None
        self.right = None
        


class Tree:
    def __init__(self):
        self.root = None

    # Time Complexity: 
    # Space Complexity: 
    def add(self, key, value = None):
        if self.root == None:
            tree = TreeNode(key, value)
        
            

            


    # Time Complexity: 
    # Space Complexity: 
    def find(self, key):
        if self.root == None:
            return None
        else:
            current = self.root

            while current:
                if current.key == key:
                    return current.value
                elif current.key < key:
                    current = current.right
                else:
                    current = current.left


    # Time Complexity: 
    # Space Complexity: 
    def inorder(self):
        if self.root == None:
            return []
        else:
            def order_nodes(current_node, array):
                if current_node:
                    self.order_nodes(current_node.left, array)
                    array.append(key=current_node.key, value=current_node.value)
                    self.order_nodes(current_node.right, array)           

            ordered_list = []
            current = self.root
            return order_nodes(current, ordered_list)
        
        
    # Time Complexity: 
    # Space Complexity:     
    def preorder(self):
        pass

    # Time Complexity: 
    # Space Complexity:     
    def postorder(self):
        pass

    # Time Complexity: 
    # Space Complexity:     
    def height(self):
        pass


#   # Optional Method
#   # Time Complexity: 
#   # Space Complexity: 
    def bfs(self):
        pass

        


#   # Useful for printing
    def to_s(self):
        return f"{self.inorder()}"
