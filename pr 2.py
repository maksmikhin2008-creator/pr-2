# 1. Односвязный список с reverse()
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class SinglyLinkedList:
    def __init__(self):
        self.head = None

    def append(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            return
        cur = self.head
        while cur.next:
            cur = cur.next
        cur.next = new_node

    def reverse(self):
        prev = None
        cur = self.head
        while cur:
            nxt = cur.next
            cur.next = prev
            prev = cur
            cur = nxt
        self.head = prev

    def print_list(self):
        cur = self.head
        while cur:
            print(cur.data, end=" -> ")
            cur = cur.next
        print("None")


sll = SinglyLinkedList()
sll.append(1)
sll.append(2)
sll.append(3)
print("SinglyLinkedList:")
sll.print_list()
sll.reverse()
print("Reversed:")
sll.print_list()


# 2. Кольцевой односвязный список
class CircularNode:
    def __init__(self, data):
        self.data = data
        self.next = None

class CircularLinkedList:
    def __init__(self):
        self.tail = None

    def append(self, data):
        new_node = CircularNode(data)
        if not self.tail:
            self.tail = new_node
            new_node.next = new_node
        else:
            new_node.next = self.tail.next
            self.tail.next = new_node
            self.tail = new_node

    def get_head(self):
        return self.tail.next if self.tail else None

    def print_list(self, count=10):
        if not self.tail:
            print("Empty")
            return
        cur = self.get_head()
        for _ in range(count):
            print(cur.data, end=" -> ")
            cur = cur.next
        print("...")


cll = CircularLinkedList()
cll.append(1)
cll.append(2)
cll.append(3)
print("\nCircularLinkedList:")
cll.print_list()


# 3. Двусвязный список с delete_tail()
class DoublyNode:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None

class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def append(self, data):
        new_node = DoublyNode(data)
        if not self.tail:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.prev = self.tail
            self.tail.next = new_node
            self.tail = new_node

    def delete_tail(self):
        if not self.tail:
            return None
        data = self.tail.data
        if self.head == self.tail:
            self.head = None
            self.tail = None
        else:
            self.tail = self.tail.prev
            self.tail.next = None
        return data

    def print_list(self):
        cur = self.head
        while cur:
            print(cur.data, end=" <-> ")
            cur = cur.next
        print("None")


dll = DoublyLinkedList()
dll.append(10)
dll.append(20)
dll.append(30)
print("\nDoublyLinkedList:")
dll.print_list()
print("Delete tail:", dll.delete_tail())
dll.print_list()
