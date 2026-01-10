# Python CLI Todo Application (Built with Claude Code CLI)

This repository contains a **CLI-based Todo Application written in Python**, generated and enhanced step by step using **Claude Code CLI** inside **Visual Studio Code**.

The project demonstrates a structured, instruction-driven AI development workflow, where all code generation follows a predefined rule set stored in `CLAUDE.md`.

---

## 📌 Project Objective

The goal of this project was to:

- Build a beginner-friendly Python CLI Todo app
- Maintain clean, modular, and readable code
- Use AI responsibly with strict instructions
- Improve the application incrementally without breaking features
- Keep task data persistent and consistent
- Demonstrate a real-world AI-assisted development process

---

## 🛠️ Tools Used

- **Python 3**
- **Visual Studio Code (VS Code)**
- **Claude Code CLI**
- **JSON file storage**

---

## 📂 Project Structure

├── main.py # CLI interface and user interaction
├── tasks.py # Task logic and operations
├── storage.py # Data persistence (load/save)
├── tasks.json # Stored task data
├── CLAUDE.md # Instruction and style guide
└── README.md # Project documentation


---

## 🧭 Complete Development Process (Exact Prompts Used)

Below is the **exact sequence of prompts** used to generate and improve this application.  
Each step builds on the previous one.

---

## 🔹 Prompt 1 – Creating the Instruction File

This was the foundation of the entire project.

create a file name CLAUDE.md this file can serve as an ultimate instructions and style guide for generating all types of apps include in a file details,beginner-friendly insturctions that should follow every time code is generated the instructions must cover the modular code structure with funcations for each operations,optional use of simple task class and dictionaries for tasks,separate file roles conceptually(main.py for CLI/menu,task.py for task logic,storage.py for data handling and file persistance,meaningful variables names and clean readable beginner friendly code,full type hints for all funcations,line by line comments explaning each logical step,robust error handling including input validation,prevention of duplicate tasks where applicable consistant tasks even after deletion or updates,optional saving/loading tasks in files with clear instructions, CLI menu rules that are clear,simple,and beginner friendly with feedback messages (advanced formatting and colour can be added later),testing and validation reminders to run after changes and check each funcation work as expected,and additional beginner friendly rules to maximize readability,maintainability, and reduce runtime errors,Make the insturctions step by step,detailed and easy so that any future code generation can reference to CLAUDE.md file for all rules and best pratices and ensure the tone is professional,clear and highly organized


This prompt created `CLAUDE.md`, which became the **single source of truth** for all future code generation.

---

## 🔹 Prompt 2 – Refining Instruction Rules

make the changes and updated the CLAUDE.md file that do not print errors and return default values instead raise exception or return Optional values use the exception raising rule and avoid absolute rules use prefer or recommended instead of always or every


This step improved code safety and professionalism by:
- Avoiding silent failures
- Preferring exceptions or Optional returns
- Removing rigid absolute wording

---

## 🔹 Prompt 3 – Generating the Initial Todo App

By using the CLAUDE.md generate a CLI based Todo app and name create a file main.py this file should be the entry point of
the app and display the following menu ========TODO APP====== 1.Add task, 2.list tasks,3.Mark tasks completed,4.Update
tasks,5.Delete task,0.Exit , choose an option make sure keep it simple and clean


### Result:
Claude Code automatically generated:
- `main.py`
- `tasks.py`
- `storage.py`
- `tasks.json`

All files followed the rules defined in `CLAUDE.md`.

---

## 🔹 Prompt 4 – Adding Task Status System

Claude, update "tasks.py" to add a task status system. Each task should have a "status" field with values "pending", "in-progress", or "completed" (default "pending"). Add functions to create tasks with status, update status, and mark completed. Use type hints, clear line-by-line comments, beginner-friendly code, and handle invalid task IDs gracefully. Do not modify main.py or storage.py.


This introduced structured task states without affecting the CLI or storage layer.

---

## 🔹 Prompt 5 – Adding Status-Based Filters

Claude, update "tasks.py" to add filter functions that return tasks by status: completed, pending, or in-progress. Each function should take the task list and return only matching tasks. Use type hints, clear line-by-line comments, beginner-friendly code, and handle empty lists gracefully. Do not modify main.py or storage.py.


Filtering logic was added cleanly and safely.

---

## 🔹 Prompt 6 – Adding Optional Task Fields

Claude, update "tasks.py" to add optional fields for each task: due_date, completed_at, and reminder_time. Update functions to set and update these fields when tasks are created or completed. Use type hints, clear line-by-line comments, beginner-friendly code, and handle empty or invalid inputs gracefully. Do not modify main.py or storage.py yet.


This step enhanced task metadata while keeping backward compatibility.

---

## 🔹 Prompt 7 – Improving CLI Layout

Claude, update "main.py" to improve the CLI Todo app layout. Make the menu clean, clear, and visually appealing with proper spacing, section headers, and optional colors for task status (pending, in-progress, completed). Ensure prompts and feedback messages are user-friendly, beginner-friendly, and easy to read. Keep code readable, add line-by-line comments, and do not modify tasks.py or storage.py.


The CLI became more readable and user-friendly.

---

## 🔹 Prompt 8 – Connecting All Features to the CLI

Claude, update "main.py" to implement all task features from tasks.py: add, list, update, delete, mark tasks (pending, in-progress, completed), filters, search by keyword, due dates, completion dates, and optional reminders. Make the CLI menu clean, clear, beginner-friendly, with proper spacing, section headers, prompts, feedback messages, and optional colors for task status. Keep code readable, add line-by-line comments, use type hints, and handle invalid inputs gracefully. Ensure all task interactions call functions from tasks.py and saving/loading from storage.py is supported.


At this stage, the application became fully functional.

---

## 🔹 Prompt 9 – Enhancing Menu Usability

"Claude, enhance the CLI menu layout for my Python Todo app. Keep the existing structure with numbered options, header, separators, and colors, but make the following improvements: align single- and double-digit numbers consistently, add a small instruction below the menu like 'Choose option (0-10) and press Enter', optionally highlight critical actions (Delete, Exit) in red, keep non-destructive actions in blue/cyan, and optionally add a footer note 'All changes auto-saved after every operation'. Keep the code clean, beginner-friendly, and fully commented so anyone can understand the formatting logic."


This improved usability and clarity for end users.

---

## 🔹 Prompt 10 – Implementing Sequential Task IDs

“Claude, update the existing code in main.py and task.py so that task IDs are simple, sequential, and human-readable (1, 2, 3, …) instead of random or UUID-based values. Ensure each task is assigned a new numeric ID at creation that is always the next available number. When tasks are deleted, do not reuse old IDs — maintain gaps in numbering to keep IDs consistent and trackable. Update all related functions (add, find, update, delete, search, filter, view) to work correctly with numeric task IDs. Keep the code beginner-friendly, fully type-hinted, well-commented line by line, and ensure no breaking changes to existing features.”


This finalized the task identity system while preserving data integrity.

✅ Final Summary

This project is a complete example of instruction-driven AI development, where:
Every change is controlled by prompts
Code quality is enforced through a guide
Features are added incrementally
No breaking changes are introduced
The final result is clean, readable, and maintainable
