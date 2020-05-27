
# Author :: Anshuman Tiwari
# Contact :: ansh1999@outlook.com

class Node:
    def __init__(self,data):
        self.data = data
        self.next = None
        self.prev = None

class CircularLinkedList:
    def __init__(self):
        self.head = None
    
    def append(self,data):
        new_node = Node(data)
        temp = list.head
        while(temp.next != list.head):
            temp = temp.next
        new_node.next = temp.next
        temp.next = new_node
        new_node.prev = temp
        new_node.next.prev = new_node

    def add(self,data,value):
        temp = list.head
        new_node = Node(data)
        while(temp.data != value):
            temp=temp.next
        new_node.next = temp.next
        temp.next = new_node
        new_node.prev = temp
        new_node.next.prev = new_node      

    def pop(self):
        temp = list.head
        while(temp.next !=list.head):
            temp = temp.next
        temp.prev.next = temp.next
        temp.next.prev =temp.prev
        print(f"Pop elemeny is :: {temp.data}")
        temp = None

    def printListFrom_Start(self):
        print("\n")
        print("Values of linked list from start ")
        temp = list.head
        print(temp.data,end = " ")
        while(temp.next != list.head):
            temp = temp.next
            print(temp.data, end = " ")
        print("\n")
    
    def printListFrom_Back(self):
        print("Values of linked list from back ")
        temp = list.head.prev
        print(temp.data,end=" ")
        while(temp.prev != list.head.prev):
            temp = temp.prev
            print(temp.data,end=" ")
        print("\n")

# program starts from here
if __name__ == "__main__":

    list = CircularLinkedList()       # created a CircularLinkedList
                      
#creating  nodes
    list.head = Node(1)               # created a head node
    sec = Node(2)
    third = Node(3)
    fourth = Node(4)

# linking all the nodes
   
    list.head.next = sec

    sec.prev = list.head
    sec.next = third

    third.prev = sec
    third.next = fourth

    fourth.prev = third
    fourth.next = list.head

    list.head.prev = fourth

# appending Node 
    list.append(10)

# adding value after node value
    list.add(15,4)                         # here 15 is the value to add and 4 is the value after which we had added 15

# pop elements
    list.pop()

# printing the list
    list.printListFrom_Start()
    list.printListFrom_Back()