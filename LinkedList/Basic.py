class Node:
    def __init__(self,value=None):
        self.value = value
        self.next = None

class LinkedList:
    def __init__(self,head=None):
        self.head = head
    def display(self):
        current_node = self.head
        while current_node:
            print(current_node.value, end=" -> ")
            current_node = current_node.next
        print("Null")

    def addBeginningNode(self,newData):
        newNode = Node(newData);
        newNode.next = self.head
        self.head = newNode

    def find_value(self,search_value):
        count=0
        current = self.head
        while current:
            if current.value == search_value:
                print(f'The value is {count}')
                count += 1
            current = current.next
        if count == 0:
            print("The value is not in list")

    def middle_node(self):
        slow=self.head
        fast=self.head
        while fast and fast.value:
            slow=slow.next
            fast=fast.next.next
        return slow.value

    def reverse(self):
        previous = None
        current = self.head
        while current:
            next = current.next
            current.next = previous
            previous = current
            current = next
        self.head = previous

li = LinkedList()
li.addBeginningNode(10)
li.addBeginningNode(20)
li.addBeginningNode(30)
li.addBeginningNode(40)
li.addBeginningNode(50)
li.addBeginningNode(60)

print(li.middle_node())
li.find_value(20)
li.reverse()
li.display()
