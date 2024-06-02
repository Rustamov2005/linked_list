
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
        # listning boshiga element qo'shish
        new_node = Node(new_data)
        new_node.next = self.head
        self.head = new_node

    def insert(self, prev_node, new_data):
        # listning ixtiyoriy nuqtasiga element qo'shish
        if prev_node is None:
            print("Error")
        # yangi element qo'shamiz
        new_node = Node(new_data)
        # yangi tugunni keyingi elementga bog'laymiz
        new_node.next = prev_node.next
        # avvalgi tugunni yangi elementga bog'laymiz
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


a = Node(5)
b = Node(6)
c = Node(7)
l_list = LinkedList()
l_list.head = a
a.next = b
b.next = c
#LinkedListnig print method
print(l_list.printList())
l_list.push(16)
#LinkedListning push method
print(l_list.printList())
l_list.insert(b, 56)
#LinkedListning innsert method
print(l_list.printList())
l_list.append(49)
#LinkedListning append method
print(l_list.printList())


data = []
for i in range(1, 11):
    data.append(i)

l_list.head = Node(data[0])
for j in data[1::]:
    l_list.push(j)
print(l_list.printList())
