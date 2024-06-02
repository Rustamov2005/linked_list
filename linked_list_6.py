
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


a = Node(64)
b = Node(128)
c = Node(256)
d = Node(512)

l_list = LinkedList()
l_list.head = a
a.next = b
b.next = c
c.next = d
#LinkedListnig print method
print(l_list.printList())
#LinkedListning push method
l_list.push(151254)
print(l_list.printList())
#LinkedListning innsert method
l_list.insert(c, 54698)
print(l_list.printList())
#LinkedListning append method
l_list.append(56987)
print(l_list.printList())

data = []
for i in range(1, 16):
    data.append(i)

l_list.head = Node(data[0])
for j in data[1::]:
    l_list.append(j)
print(l_list.printList())
