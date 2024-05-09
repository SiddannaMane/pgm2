import random
class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
        self.prev=None
        
class doubly_linked_list:
    def __init__(self):
        self.head=None

#Adding data element
    
    def insert_item(self,NewVal):
        NewNode=Node(NewVal)
        NewNode.next = self.head
        if self.head is not None:
            self.head.prev = NewNode
        self.head=NewNode
    
    def remove_item(self,NewVal):
        NewNode=Node(NewVal)
        NewNode.next = self.head
        if self.head is not None:
            self.head.prev = NewNode
        self.head=NewNode
        
# print the doubly_linked_list
    def listprint(self,node):
        while (node is not None):
            print(node.data)
            last=node
            node=node.next
            
dllist=doubly_linked_list()
for i in range(11):
    k=random.randint(10,99)
    dllist.insert_item(k)
#dllist.push(62)
dllist.remove_item()
dllist.listprint(dllist.head)