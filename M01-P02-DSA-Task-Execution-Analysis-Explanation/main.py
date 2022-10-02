from config import create_linked_list
from src.Aggregate import Aggregate

"""
Main Driver for running the implementation flow
"""
if __name__ == "__main__":
    
    #Code for initializing the linked list from the given csv file data
    task_list = create_linked_list()
    
    #This function call will print all task ids of the tasks as pushed in the linked list
    print("Printing all nodes in task list :")
    task_list.print_linked_list()
    
    #This function call will print all task ids in reverse of the tasks as pushed in the linked list
    print("\nPrinting all nodes in task list in reverse order :")
    task_list.print_in_reverse(task_list.get_list_head())
    
    #Initializing aggregate object for performing various operations.
    aggregate_obj = Aggregate(task_list)
    
    #This function call will return task with minimum execution time and task deatils 
    min_task, min_task_time = aggregate_obj.get_minimised_timed_task()
    print(f"\nThe task details with minimum task time as {min_task_time} is {min_task}")
    
    #This function call will return task with maximum execution time and task deatils
    max_task, max_task_time = aggregate_obj.get_maximised_time_task()
    print(f"\nThe task details with maximum task time as {max_task_time} is {max_task}")
    
    #This function call will return average of all task execution times, 
    #sum of all task times and the total number fo nodes in the linked list
    average, sum_task_times, no_of_nodes = aggregate_obj.get_average_time_of_all_tasks()
    print(f"\nThe sum of time of all tasks is : {sum_task_times} and the total number of task is : {no_of_nodes}. So the average is task times is : {average}")