
# to store and load tasks from a file
import json

# it checks if a file exists before reading it
import os

#This is the file where tasks will be stored
StoredTasks= "tasks.json"

"""
This function loads tasks from the JSON file
It returns an empty list if the file doesn't exist
"""
def generate_tasks():
    if os.path.exists(StoredTasks):
        with open(StoredTasks, "r") as f:     #opens file stored in StoredTasks in read mode
            return json.load(f)
    return []

#This function saves tasks to the JSON file.
def stored_tasks(tasks):
    with open(StoredTasks, "w") as f:     #opens file stored in StoredTasks in write mode
        json.dump(tasks, f, indent=2)     #writes into the file, indenting makes it easy to read


#Function to add new task to the tasks list
def add_task(tasks):
    
    title = input("Enter task: ").strip()     #prompts a user to write a task
    due_date = input("Enter due date (for example, 2000-06-29): ").strip()     #prompts a user to write when a taskis due

    if not title:
        print("Error!! Task description or due date cannot be empty.")
        return

    task = {
        "S/No": len(tasks) + 1,     #Assign each task a unique serial number
        "Title": title,
        "Due_date": due_date,
        "completed": False
    }

    tasks.append(task)     #adds new task at the end of the list
    stored_tasks(tasks)     #writes the newly added task to the JSON file
    print("Task added!")

#Function to display tasks
def display_task(tasks):

#The message below id displayed if no task has been written to the list
    if not tasks:
        print("No tasks available")
        return

    print("\nMy To-Do List:")    #list tittle

    print("-" * 50)    #prints horizontal separator line made up of 50 dashes(-)
    for task in tasks:

        status = "✔ Completed" if task["completed", False] else "✘ Pending"    #✔ will show a completed task while ✘ will show task is incomplete 

        print(f"S/No: {task['S/No']}")
        print(f"Task: {task['Title']}")
        print(f"Due Date: {task['Due_date']}")
        print(f"Status: {status}")
        print("-" * 50)     #prints horizontal separator line made up of 50 dashes(-)
    
#Function to mark task as completed using their serial number
def mark_taskComplete(tasks):

    try:
        task_sno = int(input("Enter task Serial number(S/No): "))
    except ValueError:
        print("Error! Please enter a valid serial number")
        return

    for task in tasks:
        if task["S/No"] == task_sno:
            task["Completed"] = True
            stored_tasks(tasks)     #saves update to the JSON file
            print("Marked as complete!")
            return

    print("Error! Task serial number not found.")

#Function to delete tasks using their serial number
def del_task(tasks):
    
    try:
        task_sno = int(input("Enter task serial number (S/No): "))
    except ValueError:
        print("Error! Please enter a valid serial number")
        return

    for task in tasks:
        if task["S/No"] == task_sno:
            tasks.remove(task)       #deletes task whose serial numer has been selected

            # Reassign serial number after a task has been deleted
            for index, task in enumerate(tasks):
                task["S/No"] = index + 1

            stored_tasks(tasks)     #saves the updates to the JSON file
            print("Task deleted!")
            return

    print("Error: Task ID not found.")

#Fuction for the program loop
def main():

    tasks =generate_tasks()     #loads tasks in the list
    
    #displays the main menu
    print("\nTask Management System")
    print("1. Add Task")
    print("2. View Tasks")
    print("3. Mark Task as Completed")
    print("4. Delete Task")
    print("5. Exit")

    while True:
        
        #Allows user to choose the command they wish to achieve
        choice = input("Choose an option: ")
        
        if choice == "1":
            #desc = input("Enter task name: ")
            add_task(tasks)
        elif choice == "2":
            display_task(tasks)
        elif choice == "3":
            #number = int(input("Enter task number: "))
            mark_taskComplete(tasks)
        elif choice == "4":
            del_task(tasks)
        elif choice == "5":
            print("Bye!")
            break
        else:
            print("Invalid choice! Try again.")

if __name__ == "__main__":
    main()
    
