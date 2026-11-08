tasks = []
while True:
    print("\n" + "=" * 60)
    print("               WELCOME TO THE TO-DO LIST APP ")
    print("=" * 60)
    print("            To-Do List Menu:")
    print("1. Add a task")
    print("2. View tasks")
    print("3. Remove a task")
    print("4. Mark/Unmark a Task")
    print("5. Exit")
    print()

    choice = input("   Enter your choice (1-5): ")
    print("-" * 60)

    if choice == "1":
        task_input = input("Enter task(s), separated by commas: ")
        new_tasks = [task.strip() for task in task_input.split(",") if task.strip()]
        tasks.extend({"task": task, "completed": False} for task in new_tasks)
        print()
        print(f"{len(new_tasks)} task(s) added successfully.")
        print("-" * 60)
    elif choice == "2":
        if not tasks:
            print("No tasks in the list.")
        else:
            print("Tasks:")
            for i, task in enumerate(tasks, start=1):
                print(f"{i}. {task['task']}")
            print("-" * 60)
    elif choice == "3":
        if not tasks:
            print("-" * 60)
            print("No tasks to remove.")
            print("-" * 60)
        else:
            print("-" * 60)
            # Display all tasks with their indices first
            for i, task in enumerate(tasks, start=1):
                print(f"{i}. {task['task']}")
                print()
            task_num = int(input("Enter the task number to remove: "))
            if 1 <= task_num <= len(tasks):
                removed_task = tasks.pop(task_num - 1)
                print("-" * 60)
                print(f'{removed_task["task"]} has been removed.')
                print("-" * 60)
            else:
                print("Invalid task number.")
                print("-" * 60)
    elif choice == "4":
        if not tasks:
            print("No tasks found.")
            print("-" * 60)
        else:
            print("Tasks:")
            for i, task in enumerate(tasks, start=1):
                status = "✅" if task["completed"] else "❌"
                print(f"{i}.{task['task']}  [{status}] ")
            print("-" * 60)
            task_input = input("Enter task number(s) to mark/unmark, separated by commas: ")
            print()
            task_numbers = []
            for value in task_input.split(","):
                try:
                    task_num = int(value.strip())
                except ValueError:
                    continue
                if 1 <= task_num <= len(tasks) and task_num not in task_numbers:
                    task_numbers.append(task_num)

            if task_numbers:
                for task_num in task_numbers:
                    selected_task = tasks[task_num - 1]
                    selected_task["completed"] = not selected_task["completed"]
                print("\nUpdated tasks:")
                for i, task in enumerate(tasks, start=1):
                    status = "✅" if task["completed"] else "❌"
                    print(f"{i}. {task['task']} [{status}]")
                print("-" * 60)
            else:
                print("Invalid task number.")
                print("-" * 60)
    elif choice == "5":
        print("-" * 60)
        print("Exiting the To-Do List application.")
        print("Thank you for using the app!")
        print("Bye bye! 👋")
        print("-" * 60)
        break
    else:
        print("Invalid choice. Please enter a number between 1 and 5.")
        print("-" * 60)