# 3)	Build a to-do list manager that
# •	Allows users to add tasks with priorities (e.g., "Buy milk - high").
# •	Lets them view the current list, delete tasks by number, and mark tasks as complete.
# •	Keeps looping until the user types “exit”.
# •	Shows a summary at the end: number of completed tasks vs pending.



tasks = []

while True:
    print("\nTo-Do List Manager")
    print("1. Add Task")
    print("2. View Tasks")
    print("3. Delete Task")
    print("4. Mark Task as Complete")
    print("5. Exit")

    choice = input("Choose an option or type 'exit': ").strip().lower()

    if choice == "1":
        task_input = input(
            "Enter task and priority (e.g., 'Buy milk - high'): "
        ).strip()

        if " - " in task_input:
            task, priority = task_input.split(" - ", 1)

            if task and priority:
                tasks.append({
                    "task": task,
                    "priority": priority,
                    "completed": False
                })
                print(f"Task '{task}' added with priority '{priority}'.")
            else:
                print("Task and priority cannot be empty.")
        else:
            print("Invalid format. Please use 'Task - Priority'.")

    elif choice == "2":
        if not tasks:
            print("No tasks in the list.")
        else:
            print("\nCurrent Tasks:")

            for idx, task in enumerate(tasks, start=1):
                status = "Completed" if task["completed"] else "Pending"
                print(
                    f"{idx}. {task['task']} - "
                    f"{task['priority']} [{status}]"
                )

    elif choice == "3":
        if not tasks:
            print("No tasks to delete.")
        else:
            try:
                task_num = int(input("Enter the task number to delete: "))

                if 1 <= task_num <= len(tasks):
                    removed_task = tasks.pop(task_num - 1)
                    print(f"Task '{removed_task['task']}' deleted.")
                else:
                    print("Invalid task number.")

            except ValueError:
                print("Please enter a valid integer.")

    elif choice == "4":
        if not tasks:
            print("No tasks to mark as complete.")
        else:
            try:
                task_num = int(
                    input("Enter the task number to mark as complete: ")
                )

                if 1 <= task_num <= len(tasks):
                    task = tasks[task_num - 1]

                    if not task["completed"]:
                        task["completed"] = True
                        print(f"Task '{task['task']}' marked as complete.")
                    else:
                        print("This task is already completed.")
                else:
                    print("Invalid task number.")

            except ValueError:
                print("Please enter a valid integer.")

    elif choice == "5" or choice == "exit":
        break

    else:
        print("Invalid option. Please try again.")

# Final summary
completed = sum(1 for task in tasks if task["completed"])
pending = len(tasks) - completed

print("\nTo-Do List Summary")
print(f"Completed tasks: {completed}")
print(f"Pending tasks: {pending}")
print(f"Total tasks: {len(tasks)}")
print("Goodbye!")
