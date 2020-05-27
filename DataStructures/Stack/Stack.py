
# Author :: Anshuman Tiwari
# Contact :: ansh1999@outlook.com

# adding        removing
# element       element
# \        /
#  \      /
#   \    /
# |        |       <--  tail
# |________|
# |        |  <===  elements
# |________| 
# |        |
# |________|        <--  head         we cannot use the head so we will use tail to reomve and add elements
 

class Node:
    def __init__(self,data):                 
        self.data = data
        self.next = None

class Stack:
    def __init__(self):
        self.head = None
     
    def push(self,data):
        if s.head is None:
            s.head = Node(data)
        
        else:
            new_node = Node(data)
            new_node.next = s.head
            s.head = new_node
    
    def pop(self):
        if s.head is None:
            return
        else:
            pop_node = s.head
            s.head = s.head.next
            print("popped node data is ",pop_node.data)
            print("\n")
            pop_node .next = None

    def isEmpty(self):
        if s.head is None:
            print("Stack is empty")
        else:
            print("stack has some element \n")

    def peek(self):
        temp = s.head
        print("top Value is ::",temp.data)

    def length(self):
        temp = s.head
        c = 0
        while temp is not None:
            c +=1 
            temp = temp.next
        print("length of stack is ::",c)

    def search(self,value):
        temp = s.head
        pos = 0
        while temp is not None:
            pos +=1
            if(temp.data == value):
                print("Value found at position :: ",pos)
                break
            else:
                temp = temp.next        

    def display_stack(self):
        temp = s.head
        while temp is not None:           
            print(temp.data)
            print("⇓")
            temp = temp.next
        print("\n")
    

if __name__ == "__main__":
    s = Stack()

    s.push(1)
    s.push(2)
    s.push(3)
    s.push(4)
    s.push(5)

    s.pop()                        # delete top element

    s.isEmpty()                    # print whether stack is empty or not

    s.length()                     # prints length of stack
 
    s.peek()                       # prints top element

    s.search(2)                    # searches value in the stack

    s.display_stack()              # prints all the values in the stack
