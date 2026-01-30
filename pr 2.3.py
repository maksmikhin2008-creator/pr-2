class DoublyNode:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None

class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
    
    def delete_tail(self):
        if self.tail is None:
            return None
        deleted_data = self.tail.data
        
        if self.head == self.tail:
            self.head = None
            self.tail = None
        else:
            new_tail = self.tail.prev
            new_tail.next = None
            self.tail = new_tail
        
        return deleted_data
    
    def append(self, data):
        new_node = DoublyNode(data)
        
        if self.tail is None:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.prev = self.tail
            self.tail.next = new_node
            self.tail = new_node