
# simple LinkedList 
# Author :: Anshuman Tiwari
# Contact :: anshd1999@outlook.com


class Node:                    
    def __init__(self,data):              # created a node with any object
        self.data = data
        self.next = None

class linkedlist:                         # class linkedlist
    def __init__(self):
        self.head = None 

    def push(self,data):                  # add node in beginning
        new_node = Node(data)
        new_node.next = list.head
        list.head = new_node

    def Print(self):                      # funtion to transverse over linkedlist
        temp = self.head
        while(temp):
            print(temp.data)
            temp = temp.next

    def add_node_after(self,data,prev_node):          # function to add node
        new_node = Node(data)
        new_node.next = prev_node.next
        prev_node.next = new_node  

    def append_node(self,data):                       # appending node at last
        new_node = Node(data)
        if list.head is None:
            list.head = new_node
            return
        last_node = list.head
        while(last_node.next is not None):
            last_node = last_node.next
        last_node.next = new_node   

    def delete_node_value(self,value):
        temp = list.head                             # store head
                                                    # if head contains the value to be deleted
        if(temp is not None):
            if(temp.data == value):
                list.head = temp.next
                temp = None
                return
        while(temp is not None):
            if(temp.data == value):
                break
            prev = temp
            temp = temp.next
        if(temp is None):
            return
        prev.next = temp.next
        temp = None    

    def linkedlist_length(self):
        c = 0
        temp = self.head                           # store head in temporary
        while(temp is not None):
            c=c+1
            temp = temp.next
        print(f"Length of LinkedList is {c}")

    def search(self,value_toSearch):
        c = 0
        temp = list.head
        while(temp != None):
            c +=1
            if(temp.data == value_toSearch):
                print(f"Element found at position {c}")
            temp = temp.next

    def Middle(self):                               # creating two variables and making them as head
        second = list.head
        first = list.head

        if(list.head != None):
            while(first != None and first.next != None):
                first = first.next.next
                second = second.next
            print(f"Middle Element of Linked List is {second.data}")

    def delete_linkedList(self):
        temp = list.head
        while(temp):
            ah = temp.next
            del temp.data
            temp = ah

    def reverse(self):
        prev = None
        current = list.head
        Next = None
        while current is not None:
            Next = current.next
            current.next = prev
            prev = current
            current = Next
        list.head = prev
  
# program starts from here ::

if __name__ == "__main__":

# creating a linked list
    list = linkedlist()

#creating and linking nodes
    list.head = Node(1)
    sec  = Node(2)
    third = Node(3)
    list.head.next = sec
    sec.next = third

# adding a node in linked list
    list.add_node_after(2.5,sec)
    list.add_node_after(3.5,third)

# add node at beginning
    list.push(0)

# appending node
    list.append_node(4)
    list.append_node(5)

# deleting a node
    list.delete_node_value(2)

# print length of linkedlist
    list.linkedlist_length()

# search element in linkedlist
    list.search(2.5)

# print Middle Element of Linked List
    list.Middle()

# delete all data from Linked List
    # list.delete_linkedList()     
    #  just remove '#' to comment out

# reverse a list
   # list.reverse()

# linkedlist transversal print
    list.Print()