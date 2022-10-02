from src.LinkedList import Node, LinkedList
import csv

"""
This function is responsible for creating the linked list after reading the various tasks details mentioned
in the csv file
As a part of task details we will be reading the following details from the each row:
    1. Task ID
    2. Start Time
    3. End Time
"""
def create_linked_list():
    
    #Initializing the LinkedList object
    task_list = LinkedList()
    
    #Reading data from csv file and creating the linked list
    with open('tasks.csv', newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            start_time = convert_time_to_int(row['Start Time'])
            end_time  = convert_time_to_int(row['End Time'])
            
            node  = Node(row['Task ID'], start_time, end_time)
            task_list.insert_node(node, 1)
            
    return task_list


"""
This function is responsible for converting the time to equivalent integer format for further processing
"""
def convert_time_to_int(time):
    time = time.replace(':', '')
    return int(time)