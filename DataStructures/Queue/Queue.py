# Author :: Anshuman Tiwari
# Contact :: anshd1999@outlook.com

class Node:
    def __init__(self,data):
        self.data = data
        self.next = None
        
class Queue:
    def __init__(self):
        self.head = None

    def Enqueue(self,data):
        temp = Node(data)
        last_node = q.head 

        if q.head is None:
            q.head = temp
        else:
            while(last_node.next is not None):
                last_node = last_node.next
            last_node.next = temp

                
    def DeQueue(self):
        if q.head is None:
            return
        else:
            print("De- Queued value is :: ", q.head.data)
            temp = q.head 
            q.head = None
            q.head = temp.next
            
                    

    def print_queue(self):
        temp = q.head
        c = 0 
        while temp is not None:
            c +=1
            print(temp.data)
            temp = temp.next    
        print("length of Queue is :: ",c)   

    def Search_For(self,value):
        temp = q.head
        c = 1
        while temp is not None:
            if(temp.data == value):
                print(f"Value {value} found at poisition {c}")
                break
            else:
                c +=1
                temp = temp.next

if __name__ == "__main__":
    q = Queue()
    
    q.Enqueue(7)
    q.Enqueue(6)
    q.Enqueue(5)
    q.Enqueue(4)
    q.Enqueue(3)
    q.Enqueue(2)
    q.Enqueue(1)

    q.DeQueue()
    q.DeQueue()

    q.Search_For(2)

    q.print_queue()