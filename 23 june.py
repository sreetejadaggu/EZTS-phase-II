class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
class CLL:
    def __init__(self):
        self.head=None
        self.tail=None
    def display(self):
        if self.head is None:
            print("empty")
        else:
            temp=self.head
            print(temp.data)
            while temp.next != self.head:
                print(temp.data)
                temp=temp.next
                print(temp.next.data)
node_1=Node(10)
node_2=Node(20)
node_3=Node(30)
node_4=Node(40)
node_5=Node(50)
node_6=Node(60)
print(node_1)
print(node_2)
print(node_3)
cl=CLL()
cl.head=node_1
cl.tail=node_1
cl.tail.next=cl.head
print(cl.tail.next)
node_1.next=node_2
cl.tail=node_2
cl.tail.next=cl.head
print(node_1.next)
print(cl.tail.next)
print(node_2.next)
node_2.next=node_3
cl.tail=node_3
cl.tail.next=cl.head
node_3.next=node_4
cl.tail=node_4
cl.tail.next=cl.head
node_4.next=node_5
cl.tail=node_5
cl.tail.next=cl.head
node_5.next=node_6
cl.tail=node_6
cl.tail.next=cl.head
cl.display()
"""
INSERTION
create a node
connect to current head
change head to new node
connect tail next to current head
"""
def insert_beginning(self,data):
    new_node=Node(data)
    if self.head is None:
        self.head=new_node
        self.tail=new_node
        self.tail.next=self.head
    else:
        new_node.next=self.head
        self.head=new_node
        self.tail.next=self.head
cl.insert_beginning(70)
cl.display()
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
    def insert_pos(self,pos,data):
        new_node=Node(data)
        if self.head is None:
             self.head=new_node
             self.tail=new_node
             self.tail.next=self.head
        else:
            if pos==1:
                insert_beginning(data)
            else:
                temp=self.head
                for i in range(1,pos-1):
                    temp=temp.next
                new_node.next=temp.next
    
       

