
# Author :: Anshuman Tiwari
# Contact :: ansh1999@outlook.com

class Node:                                  # Creating a Node
    def __init__(self,data):                 
        self.data = data                     # Create data for node
        self.prev = None                     # Create previous link for nodes
        self.next = None                     # Created next link for Nodes

class DoublyLinkedList:
    def __init__(self):
        self.head = None

    def print_list(self):
        temp = list.head
        while(temp != None):
            print(temp.data)
            temp = temp.next

    def push(self,value_to_Add):
        temp = Node(value_to_Add)
        temp.prev = None

        if list.head is None:
            list.head = temp 

        if list.head is not None:
            temp.next = list.head
            list.head.prev = temp
            list.head = temp

    def append(self,value_to_Append):
        temp = Node(value_to_Append)
        temp.next = None

        if list.head is None:
            temp.prev = None
            list.head = temp
                    
        if list.head is not None:
            last = list.head
            while(last.next is not None):
                last =last.next
            last.next = temp
            temp.prev = last       

    def insertAfter(self,prev_node,data_toInsert):
        temp = Node(data_toInsert)
        if prev_node is None:
            return
        if prev_node is not None:
            temp.next = prev_node.next
            prev_node.next = temp
            temp.prev = prev_node
        if(temp.next is not None):
            temp.next.prev = temp

    def delete_value(self,value_toDelete):
        if list.head is None or value_toDelete is None:
            return
        if list.head.data == value_toDelete:
            list.head.next = list.head
            list.head.prev = None

        temp = list.head
        
        while(temp.data != value_toDelete):
            temp = temp.next

        previous = temp.prev
        previous.next = temp.next 
        temp.next.prev = previous

    def add_node(self,pos,value):
        temp = list.head
        c=1
        while(temp != None):
            temp = temp.next
            c = c+1
        if pos == 0:
            list.push(value)
        if pos == c:
            list.append(value)
        else:
            node_pos = list.head
            for _ in range(pos-2):
                node_pos = node_pos.next
            new_node = Node(value)
            new_node.next = node_pos.next
            node_pos.next = new_node
            new_node.prev = node_pos
            new_node.next.prev = new_node

    def search_for(self,value):
        c = 1
        temp = list.head       
        while(temp.data != value):
            temp = temp.next
            c +=1
        print(f"Value found at pos {c} in the list")

    def reverse(self):
        temp = None
        current = list.head
        while current is not None:
            temp = current.prev
            current.prev = current.next
            current.next = temp 
            current = current.prev
        if temp is not None:
            list.head = temp.prev

# program starts from here ::

if __name__ == "__main__":

    list = DoublyLinkedList()                     # object for class Doubly Linked List
    list.head = Node(1)                           # created a head node
    sec = Node(2)
    third = Node(3)
    fourth = Node(4)

# linking all the nodes
    list.head.prev = None
    list.head.next = sec

    sec.prev = list.head
    sec.next = third

    third.prev = sec
    third.next = fourth

    fourth.prev = third
    fourth.next = None

# adding value in beggining
    list.push(0)

# appeding value to list
    list.append(5)

# add value after node 
    list.insertAfter(sec,2.5)

# delete value in the list
    list.delete_value(2)

# create a node
    list.add_node(4,10)
    list.add_node(7,11) 
    list.add_node(8,12)    
    list.add_node(10,21) 

# search value in the list
    list.search_for(2.5)

# reverse the list
    list.reverse()

# printing list data
    list.print_list()

