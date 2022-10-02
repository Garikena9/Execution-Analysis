"""
Node Class:
    This is responsible for storing task details in the class and can be added to linked list
"""
class Node:
    #Constructor Implementation
    def __init__(self,Task_id,start_time,end_time):
        pass
        self.task_id = Task_id
        self.start_time = start_time
        self.end_time = end_time
        self.next = None
        
"""
LinkedList Class:
    This is responsible for implementing Linked List for the tasks and is used for implementing
    various aggregate operations.

"""
class LinkedList:
    #Constructor Implementation
    def __init__(self):
        self.head = None
        
    #This method will return the head of the linked list
    def get_list_head(self):
        return self.head
    
    #This method is responsible for printing the linked list nodes
    def print_linked_list(self):
        temp = self.head
        while (temp != None):
            print(temp.task_id, temp.start_time, temp.end_time,'\n', end=" ")
            temp = temp.next
    pass
            
    #This method is responsible for inserting node in the linked list 
    #in the beginning or at end based on the flag as insert_at_starting
    def insert_node(self, node:Node, insert_at_starting=0):
        node.next = self.head
        self.head = node 
        pass
    
    #This method is responsible for printing the linked list nodes in reverse order
    def print_in_reverse(self, node):
        if node:
            self.print_in_reverse(node.next)
            print(node.task_id, node.start_time, node.end_time,'\n', end =" ")
        else:
            return
        pass