import sys
from typing import List, Optional
import storage
from task import (
    Task, add_task, find_task_by_id, delete_task,
    get_pending_tasks, get_in_progress_tasks, get_completed_tasks,
    search_tasks
)

# --- ANSI Color Constants ---
BLUE = "\033[94m"
GREY = "\033[90m"
RESET = "\033[0m"
BOLD = "\033[1m"
CYAN = "\033[36m"

# --- UI Helper Functions ---

def print_header(title: str) -> None:
    """Print a clean, centered header in blue."""
    print(f"\n{BLUE}{'='*60}{RESET}")
    print(f"{BLUE}{BOLD}{title.center(60)}{RESET}")
    print(f"{BLUE}{'='*60}{RESET}")

def print_task_list(tasks: List[Task], list_title: str) -> None:
    """Display a list of tasks in a clean, grey/blue table format."""
    print_header(list_title)

    if not tasks:
        print(f"{GREY}No tasks found in this section.{RESET}")
        return

    # Header for the table
    print(f"{BLUE}{'ID':<10} {'Status':<15} {'Title':<20} {'Due Date':<12}{RESET}")
    print(f"{GREY}{'-'*60}{RESET}")

    for task in tasks:
        # Color coding status
        status_color = BLUE if task.status != "completed" else GREY
        status_text = f"{status_color}{task.status}{RESET}"

        due = task.due_date if task.due_date else "---"

        print(f"{GREY}{task.id:<10}{RESET} {status_text:<24} {task.title:<20} {GREY}{due:<12}{RESET}")

    print(f"{BLUE}{'-'*60}{RESET}")

# --- Command Handlers ---

def handle_add_task(tasks: List[Task]) -> List[Task]:
    """Gather input and add a new task with optional metadata."""
    print(f"\n{BLUE}[ ADD NEW TASK ]{RESET}")
    title = input(f"{GREY}Enter title: {RESET}").strip()
    due_date = input(f"{GREY}Enter due date (YYYY-MM-DD) [optional]: {RESET}").strip()
    reminder_time = input(f"{GREY}Enter reminder time [optional]: {RESET}").strip()

    return add_task(
        tasks,
        title,
        due_date=due_date if due_date else None,
        reminder_time=reminder_time if reminder_time else None
    )

def handle_status_update(tasks: List[Task]) -> None:
    """Find task and change its specific status."""
    task_id = input(f"\n{BLUE}Enter Task ID to update status: {RESET}").strip()
    task = find_task_by_id(tasks, task_id)

    if not task:
        print(f"{GREY}Error: Task not found.{RESET}")
        return

    print(f"\n{BLUE}Select New Status:{RESET}")
    print(f"{BLUE}1.{RESET} pending")
    print(f"{BLUE}2.{RESET} in-progress")
    print(f"{BLUE}3.{RESET} completed")

    choice = input(f"{GREY}Choice: {RESET}").strip()
    status_map = {"1": "pending", "2": "in-progress", "3": "completed"}

    if choice in status_map:
        task.update_status(status_map[choice])
        print(f"{BLUE}Success: Status updated to {status_map[choice]}.{RESET}")
    else:
        print(f"{GREY}Skipped: Invalid selection.{RESET}")

def handle_search(tasks: List[Task]) -> None:
    """Search tasks by title keyword."""
    keyword = input(f"\n{BLUE}Search keyword: {RESET}").strip()
    results = search_tasks(tasks, keyword)
    print_task_list(results, f"Search Results: '{keyword}'")

def main() -> None:
    """Main application loop with Blue/Grey CLI theme."""
    # Data Persistence: Load tasks at startup
    task_dicts = storage.load_tasks()
    tasks = [Task.from_dict(d) for d in task_dicts]

    while True:
        # Clean Menu UI
        print(f"\n{BLUE}{BOLD}======== TODO MANAGER ========{RESET}")
        print(f"{BLUE}1.{RESET}  Add Task")
        print(f"{BLUE}2.{RESET}  List All Tasks")
        print(f"{BLUE}3.{RESET}  Mark as Completed")
        print(f"{BLUE}4.{RESET}  Update Task Title")
        print(f"{BLUE}5.{RESET}  Update Task Status")
        print(f"{BLUE}6.{RESET}  Delete Task")
        print(f"{GREY}------------------------------{RESET}")
        print(f"{CYAN}7.{RESET}  View Pending")
        print(f"{CYAN}8.{RESET}  View In-Progress")
        print(f"{CYAN}9.{RESET}  View Completed")
        print(f"{CYAN}10.{RESET} Search Tasks")
        print(f"{BLUE}0.{RESET}  Exit")
        print(f"{BLUE}=============================={RESET}")

        choice = input(f"{BOLD}Choose option: {RESET}").strip()

        if choice == "1":
            tasks = handle_add_task(tasks)
        elif choice == "2":
            print_task_list(tasks, "ALL TASKS")
        elif choice == "3":
            task_id = input(f"{BLUE}ID of task to complete: {RESET}").strip()
            task = find_task_by_id(tasks, task_id)
            if task:
                task.mark_completed()
                print(f"{BLUE}Task marked as done.{RESET}")
        elif choice == "4":
            task_id = input(f"{BLUE}ID to update title: {RESET}").strip()
            task = find_task_by_id(tasks, task_id)
            if task:
                new_title = input(f"{GREY}New title: {RESET}").strip()
                task.update_title(new_title)
        elif choice == "5":
            handle_status_update(tasks)
        elif choice == "6":
            task_id = input(f"{BLUE}ID to delete: {RESET}").strip()
            tasks = delete_task(tasks, task_id)
            print(f"{GREY}Task removed.{RESET}")
        elif choice == "7":
            print_task_list(get_pending_tasks(tasks), "PENDING TASKS")
        elif choice == "8":
            print_task_list(get_in_progress_tasks(tasks), "IN-PROGRESS TASKS")
        elif choice == "9":
            print_task_list(get_completed_tasks(tasks), "COMPLETED TASKS")
        elif choice == "10":
            handle_search(tasks)
        elif choice == "0":
            storage.save_tasks([t.to_dict() for t in tasks])
            print(f"{BLUE}Data saved. Goodbye!{RESET}")
            break
        else:
            print(f"{GREY}Invalid option.{RESET}")

        # Data Persistence: Save after every operation
        storage.save_tasks([t.to_dict() for t in tasks])

if __name__ == "__main__":
    main()
