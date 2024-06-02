
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def printList(self):
        temp = self.head
        while temp:
            print(temp.data)
            temp = temp.next

    def push(self, new_data):
        new_node = Node(new_data)
        new_node.next = self.head
        self.head = new_node

    def insert(self, prev_node, new_data):
        if prev_node is None:
            print("Error")
        new_node = Node(new_data)
        new_node.next = prev_node.next
        prev_node.next = new_node

    def append(self, new_data):
        new_node = Node(new_data)
        if self.head is None:
            self.head = new_node
            return
        last = self.head
        while last.next:
            last = last.next
        last.next = new_node


a = Node(100)
b = Node(200)
c = Node(300)
d = Node(400)

l_list = LinkedList()
l_list.head = a
a.next = b
b.next = c
c.next = d
#LinkedListnig print method
print(l_list.printList())
l_list.push(1)
l_list.push(2)
l_list.push(3)
l_list.push(4)
#LinkedListning push method
print(l_list.printList())
#LinkedListning innsert method
l_list.insert(b, 48)
print(l_list.printList())
#LinkedListning append method
l_list.append(94)
print(l_list.printList())