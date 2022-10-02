from src.LinkedList import LinkedList, Node

"""
Aggregate class is responsible for implementating various operations on the linked list
    1. Get Minimum Timed Task Details
    2. Get Maximum Timed Task Details
    3. Get Average of all the execution times of the tasks pushed in the linked list
"""
class Aggregate:
    
    #Initializing linked list object for various operations 
    def __init__(self, linked_list:LinkedList):
        self.linked_list = linked_list
    
    #Function responsible for searching the task having maximum execution time among all the tasks
    def get_maximised_time_task(self):
        temp = self.linked_list.head
        # print(f" in minimized \n {temp.print_values()} ")
        max_node = temp 
        max_value =  temp.end_time - temp.start_time
             
        while temp is not None:
            diff = temp.end_time - temp.start_time
            if diff > max_value:
                max_value = diff
                max_node = temp
            temp = temp.next
        # print(max_node == None)
        return (max_node.task_id, max_value)
    
    #Function responsible for searching the task having minimum execution time among all the tasks
    def get_minimised_timed_task(self):        
        temp = self.linked_list.head
        # print(f" in minimized \n {temp.print_values()} ")
        min_node = temp
        min_value =  temp.end_time - temp.start_time
              
        while temp is not None:
            diff = temp.end_time - temp.start_time 
            if diff < min_value:
                min_value = diff
                min_node = temp
            temp = temp.next
        # print(min_node == None)
        return (min_node.task_id, min_value)

    
    #Function responsible for calculating average of the all execution times of the tasks in the linked list
    def get_average_time_of_all_tasks(self):
        temp = self.linked_list.head 
        count = 0 
        sum = 0  
        while temp is not None:
            diff =  temp.end_time - temp.start_time
            sum = sum + diff
            count = count + 1
            temp = temp.next
        avg = sum // count
        return (avg, sum, count)
        pass
