def add_task(tasks, task):
    tasks.append({"task": task, "completed": False})

def complete_task(tasks, index):
    if 0 <= index < len(tasks):
        tasks[index]["completed"] = True

def display_tasks(tasks):
    for i, t in enumerate(tasks):
        status = "✓" if t["completed"] else "✗"
        print(f"{i}. [{status}] {t['task']}")

def main():
    tasks = []
    while True:
        print("\n1. Add Task\n2. Complete Task\n3. Show Tasks\n4. Quit")
        choice = input("Choose an option: ")

        if choice == "1":
            add_task(tasks, input("Enter task: "))
        elif choice == "2":
            complete_task(tasks, int(input("Enter task number: ")))
        elif choice == "3":
            display_tasks(tasks)
        elif choice == "4":
            break

if __name__ == "__main__":
    main()
