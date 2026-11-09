# To-Do List Application

A simple, interactive command-line to-do list application written in Python designed to help users efficiently manage daily tasks directly from the terminal.

---

## 🚀 What It Is, Why I Made It, and What It Does

### What It Is
This is a lightweight, command-line interface (CLI) task management tool built entirely in Python. It runs locally in your terminal, offering a straightforward menu-driven experience without requiring any complex database setups or external dependencies.

### Why I Made It
I built this project to practice core Python programming concepts—such as loops, conditionals, functions, and data structures (lists and dictionaries)—while creating a practical, everyday utility tool. It showcases how simple code can solve real-world productivity challenges with zero bloat.

### What It Does
The application allows you to:
- Add single or multiple tasks in one go (separated by commas).
- View your current task list with clear status indicators (pending vs. completed).
- Mark tasks as completed or revert them back to pending.
- Delete specific tasks by their index numbers.
- Keep everything running smoothly in memory during your active session.

---

## ✨ Features

* **Batch Task Addition:** Add one or multiple tasks simultaneously by separating them with commas.
* **Interactive Menu:** Navigate options easily using a clean text-based menu.
* **Task Status Tracking:** Toggle tasks between *Pending* and *Completed* states.
* **Indexed Management:** Remove or update specific tasks easily using their reference numbers.
* **In-Memory Storage:** Keeps data fast and secure during runtime.

---

## 🔄 System Flow

```text
[ Start Program ]
       │
       ▼
[ Display Main Menu ]
       │
       ├─► 1. Add Task(s) ──────► [ Parse Input & Append to Memory ]
       ├─► 2. View Tasks ───────► [ Print Formatted List with Status ]
       ├─► 3. Mark Completed ───► [ Update Task Status Flag ]
       ├─► 4. Remove Task ──────► [ Delete Task by Index Number ]
       └─► 5. Exit ─────────────► [ Terminate Program ]

🏗️ Architecture
The project follows a clean, modular procedural programming architecture contained within a single script:

Data Model: Tasks are managed using a Python list of dictionaries (storing the task description and completion status boolean).

Control Flow: A while True loop keeps the application running until the user explicitly chooses to exit.

Input Validation: Handles user selections safely to prevent crashes from invalid menu choices or out-of-range indices.

to-do-list/
├── README.md
└── To-Do-List.py

💻 Technology Used
Python 3.x: Core programming language.

Standard Library Only: Utilizes built-in Python features with zero external dependencies or third-party packages required.

⚙️ How to Run
Clone or download this repository.

Open your terminal and navigate to the project folder.

Run the application using the following command:

python To-Do-List.py

Choose an option from the interactive menu and follow the on-screen prompts.

🖥️ Example Output

==============================
     PYTHON TO-DO LIST
==============================
1. View Tasks
2. Add Task(s)
3. Mark Task as Completed
4. Remove Task
5. Exit
==============================
Select an option (1-5): 2

Enter task(s) separated by commas: Buy groceries, Pay electricity bill, Finish Python project
Tasks added successfully!

------------------------------
1. View Tasks
2. Add Task(s)
...
Select an option (1-5): 1

--- YOUR TO-DO LIST ---
1. [ ] Buy groceries
2. [ ] Pay electricity bill
3. [ ] Finish Python project

------------------------------
Select an option (1-5): 3
Enter the task number to mark as completed: 1
Task 1 marked as completed!



