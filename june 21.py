"""STACK 
stc=[]
def push_element():
    if len(stc)==n:
        print("stack is full")
    else:
        element=input("enter element for stack:")
        stc.append(element)
        print(stc)
def pop_element():
    if not stc:
        print("stack is empty")
    else:
        e=stc.pop()
        print(e,"removed")
        print(stc)
n=int(input("enter the size of stack:"))
while True:
    print("select the operation 1.push 2.pop 3.quit")
    choice=int(input())
    if choice==1:
        push_element()
    elif choice==2:
        pop_element()
    elif choice==3:
        break
    else:
        print("enter correct operation:")
"""
"""
QUEUE
queue=[]
def enqueue():
    if len(queue)==n:
        print("queue is full")
    else:
        element=input("enter element for queue:")
        queue.append(element)
        print(queue)
def dequeue():
        if not queue:
            print("queue is empty")
        else:
            e=queue.pop(0)
            print(queue)
n=int(input("enter the size of queue:"))
while True:
    print("select the operation 1.push 2.pop 3.quit")
    choice=int(input())
    if choice==1:
        enqueue()
    elif choice==2:
        dequeue()
    elif choice==3:
        break
    else:
        print("enter correct operation:")
        """
class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
class SLL:
    def __init__(self):
        self.head=None
        
