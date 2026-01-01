
#Add task

def add_task(task, description):
     task.append({"description": description, "completed": False})

#Veiw task

def display_task(task):
    print("\nYour To-Do List:")
    for i, task in enumerate(task):
        status = "✔" if task["completed"] else "✘"
        print(f"{i}. [{status}] {task['description']}")
    print()

#Mark task as completed

def mark_task_complete(task, task_number):
    if 0 <= task_number < len(task):
        task[task_number]["completed"] = True
        print("Task completed.")
    else:
        print("Task incomplete ")

def main():
    task = []
    
    while True:
        print("Task Management System")
        print("1. Add task")
        print("2. Display tasks")
        print("3. Mark task complete")
        print("4. Exit")
        
        choice = input("Choose an option: ")
        
        if choice == "1":
            desc = input("Enter task name: ")
            add_task(task, desc)
        elif choice == "2":
            display_task(task)
        elif choice == "3":
            number = int(input("Enter task number: "))
            mark_task_complete(task, number)
        elif choice == "4":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Try again.")

if __name__ == "__main__":
    main()
    
