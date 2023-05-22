class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.start = None

    def viewList(self):
        if self.start is None:
            print("List is empty")
        else:
            temp = self.start
            while temp is not None:
                print(temp.data, end = ' ')
                temp = temp.next
    
    def deleteFirst(self):
        if self.start is None:
            print("LinkedList is empty")
        else:

            self.start = self.start.next
    
    def insertLast(self, value):
        newNode = Node(value)
        if self.start is None:
            self.start = newNode
        else:
            temp = self.start
            while temp.next != None:
                temp = temp.next
            temp.next = newNode
    
mylist = LinkedList()
mylist.insertLast(10)
mylist.insertLast(20)
mylist.insertLast(30)
mylist.insertLast(40)

mylist.viewList()
print()
mylist.deleteFirst()
mylist.viewList()
input()