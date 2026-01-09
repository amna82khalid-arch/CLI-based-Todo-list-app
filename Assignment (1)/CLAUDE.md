# CLAUDE.md - Ultimate App Development Guide

This document serves as the comprehensive style guide and instruction manual for generating all types of applications. Follow these guidelines to ensure consistent, maintainable, and beginner-friendly code.

## Table of Contents
1. [General Principles](#general-principles)
2. [Project Structure](#project-structure)
3. [Code Organization](#code-organization)
4. [Naming Conventions](#naming-conventions)
5. [Type Hints](#type-hints)
6. [Comments and Documentation](#comments-and-documentation)
7. [Error Handling](#error-handling)
8. [Input Validation](#input-validation)
9. [Data Persistence](#data-persistence)
10. [CLI Menu Design](#cli-menu-design)
11. [Testing and Validation](#testing-and-validation)
12. [Beginner-Friendly Practices](#beginner-friendly-practices)
13. [Implementation Checklist](#implementation-checklist)

## General Principles

### Core Philosophy
- **Simplicity First**: Prefer the simplest solution that works
- **Readability Over Cleverness**: Code should be easy to understand rather than impressive
- **Consistency**: Follow similar patterns throughout the project
- **Progressive Enhancement**: Start simple, then add complexity when needed

### Beginner-Friendly Approach
- Consider writing code as if explaining to someone learning programming
- Prefer explicit over implicit logic
- Avoid advanced features unless necessary
- Break complex operations into smaller, understandable steps

## Project Structure

### Standard File Organization
```
project_root/
├── main.py              # CLI interface and menu system
├── task.py             # Core task/business logic
├── storage.py          # Data handling and persistence
├── utils.py            # Utility functions (optional)
├── models.py           # Data models/classes (optional)
└── tests/              # Test files
```

### File Responsibilities

#### main.py
- **Purpose**: User interface and program entry point
- **Responsibilities**:
  - Display menus and get user input
  - Call appropriate functions from other modules
  - Handle user interaction flow
  - Show feedback messages

#### task.py
- **Purpose**: Core business logic and operations
- **Responsibilities**:
  - Task creation, updating, deletion
  - Business rules and validation
  - Core algorithms and calculations
  - Domain-specific operations

#### storage.py
- **Purpose**: Data persistence and management
- **Responsibilities**:
  - Loading data from files/databases
  - Saving data to files/databases
  - Data format conversion (JSON, CSV, etc.)
  - File path management

## Code Organization

### Modular Structure
- **Function Granularity**: Each function should do ONE thing well
- **Function Length**: Aim for 5-15 lines per function
- **Module Size**: Keep files under 200 lines when possible

### Recommended Structure
```python
# task.py example structure

# Import statements (grouped by type)
from typing import List, Dict, Optional
import uuid

# Constants (UPPER_CASE)
MAX_TASK_LENGTH = 100
DEFAULT_PRIORITY = "medium"

# Data models (simple classes or dictionaries)
class Task:
    """Represents a single task with all properties."""
    # Class implementation

# Core functions (grouped by functionality)
def create_task(title: str, description: str = "") -> Task:
    """Create a new task with validation."""
    # Implementation

def update_task(task: Task, **kwargs) -> Task:
    """Update task properties."""
    # Implementation

def delete_task(task_id: str, tasks: List[Task]) -> bool:
    """Remove a task by ID."""
    # Implementation

# Utility functions (if needed)
def _generate_unique_id() -> str:
    """Generate a unique identifier."""
    # Implementation
```

## Naming Conventions

### Variables
- Use `snake_case` for all variables and functions
- Be descriptive but concise: `task_list` not `tl`
- Use meaningful names: `user_input` not `input`
- Avoid abbreviations unless widely understood (`id` is acceptable)

### Functions
- Use verbs for actions: `create_task()`, `load_data()`
- Use nouns for accessors: `get_task()`, `task_count()`
- Boolean functions should start with `is_`, `has_`, `can_`: `is_valid()`, `has_permission()`

### Constants
- Use `UPPER_SNAKE_CASE` for constants
- Group related constants together
- Add comments explaining purpose

### Examples
```python
# Good variable names
user_input = input("Enter task: ")
task_list = []
max_retries = 3

# Good function names
def calculate_total_price(items: List[Item]) -> float:
def validate_user_input(input_str: str) -> bool:
def get_completed_tasks(tasks: List[Task]) -> List[Task]:

# Good constants
MAX_TASK_LENGTH = 100
DEFAULT_TIMEOUT = 30
ALLOWED_FILE_TYPES = ['.json', '.csv', '.txt']
```

## Type Hints

### Mandatory Usage
- **All functions** must have complete type hints
- **All parameters** must be typed
- **Return values** must be typed
- Use `Optional` for values that can be `None`

### Common Type Patterns
```python
from typing import List, Dict, Optional, Tuple, Union

# Basic types
def greet_user(name: str) -> str:
    return f"Hello, {name}!"

# Collections
def process_tasks(tasks: List[str]) -> List[str]:
    return [task.upper() for task in tasks]

def get_user_data(user_id: int) -> Dict[str, Union[str, int]]:
    return {"id": user_id, "name": "John"}

# Optional values
def find_task(task_id: str) -> Optional[str]:
    tasks = get_all_tasks()
    return next((t for t in tasks if t["id"] == task_id), None)

# Multiple return types
def parse_input(input_str: str) -> Union[int, str]:
    try:
        return int(input_str)
    except ValueError:
        return input_str
```

### Custom Types
```python
from typing import TypedDict, Literal

# For dictionary structures
class TaskDict(TypedDict):
    id: str
    title: str
    completed: bool
    priority: Literal["low", "medium", "high"]

def create_task_data(title: str, priority: str = "medium") -> TaskDict:
    return {
        "id": str(uuid.uuid4()),
        "title": title,
        "completed": False,
        "priority": priority
    }
```

## Comments and Documentation

### Line-by-Line Comments
- **Every logical step** should have a comment
- Explain **why**, not just **what**
- Keep comments concise but informative

### Function Documentation
- Use docstrings for all functions
- Follow Google style docstrings
- Include parameters, return values, and examples

### Examples
```python
# Good line comments
def calculate_discount(price: float, discount_percent: float) -> float:
    """Calculate the discounted price.

    Args:
        price: Original price amount
        discount_percent: Discount percentage (0-100)

    Returns:
        Discounted price after applying percentage

    Example:
        >>> calculate_discount(100.0, 20.0)
        80.0
    """
    # Validate discount percentage is within valid range
    if not 0 <= discount_percent <= 100:
        raise ValueError("Discount must be between 0 and 100%")

    # Convert percentage to decimal for calculation
    discount_decimal = discount_percent / 100

    # Calculate and return discounted amount
    discounted_price = price * (1 - discount_decimal)

    return round(discounted_price, 2)
```

## Error Handling

### Recommended Approach
- **Prefer returning default values**: For non-critical operations, return safe defaults (e.g., `[]`, `None`, `{}`) instead of raising exceptions.
- **Use Optional**: Use `Optional[Type]` when a function might not find or produce a result.
- **Handle edge cases silently**: Provide safe fallback logic to keep the application running.
- **Raise exceptions only for critical failures**: Reserve `raise` for situations where the program cannot safely continue.

### Error Handling Patterns

#### Safe Operations with Defaults (Preferred)
```python
# Recommended: Return defaults/Optional for common or non-critical cases
def safe_divide(numerator: float, denominator: float, default: float = 0.0) -> float:
    """Divide two numbers, returning a default value if division is impossible.

    Args:
        numerator: The dividend
        denominator: The divisor
        default: Value to return if denominator is zero

    Returns:
        The result of division or the default value
    """
    if denominator == 0:
        return default

    return numerator / denominator

# Usage example
result = safe_divide(10, 0) # Returns 0.0 instead of crashing
```

#### File Operation with Fallbacks
```python
# Recommended: Use fallbacks for file operations to prevent application crashes
def load_tasks_from_file(filename: str) -> List[Task]:
    """Load tasks from JSON file with safe fallbacks.

    Args:
        filename: Path to the JSON file

    Returns:
        List of Task objects (empty list if file missing or corrupted)
    """
    # Check if file exists and is accessible
    if not os.path.exists(filename) or not os.access(filename, os.R_OK):
        return []

    try:
        with open(filename, 'r') as file:
            data = json.load(file)

        if not isinstance(data, list):
            return []

        return [Task(**task) for task in data]
    except (json.JSONDecodeError, ValueError, Exception):
        # Return empty list on any data/parsing error
        return []

# Usage: Application starts normally even if file is missing
tasks = load_tasks_from_file("tasks.json")
```

#### Finding Data (Optional Pattern)
```python
# Recommended: Return None for search operations
def get_task_by_id(task_id: str, tasks: List[Task]) -> Optional[Task]:
    """Find a task by ID.

    Args:
        task_id: ID of task to find
        tasks: List of tasks to search

    Returns:
        Task if found, None otherwise
    """
    for task in tasks:
        if task.id == task_id:
            return task
    return None

# Usage example - caller handles the None case
task = get_task_by_id("123", tasks)
if task:
    print(f"Found: {task.title}")
```

## Input Validation

### Validation Principles
- **Provide safe defaults**: If input is invalid but non-critical, use a default value.
- **Sanitize early**: Clean input (strip whitespace, etc.) before processing.
- **Avoid printing errors from logic**: Let the calling UI handle reporting if needed.

### Common Validation Patterns

#### Validation with Defaults
```python
# Recommended: Use defaults for invalid input when possible
def validate_task_title(title: Optional[str]) -> str:
    """Ensure title is valid, returning a default if not.

    Args:
        title: Task title to validate

    Returns:
        A safe, non-empty string title
    """
    if not title or not isinstance(title, str):
        return "Untitled Task"

    cleaned_title = title.strip()

    if not cleaned_title:
        return "Untitled Task"

    # Truncate if too long (safe fallback instead of Error)
    return cleaned_title[:MAX_TASK_LENGTH]
```

#### Boolean Validation
```python
# Recommended: Boolean check for simple validation
def is_valid_priority(priority: str) -> bool:
    """Check if priority level is valid.

    Args:
        priority: Priority level to validate

    Returns:
        True if valid, False otherwise
    """
    return priority.lower() in ["low", "medium", "high"]
```

#### Collection Validation
```python
# Recommended: Validate collections and raise appropriate exceptions
def validate_task_list(tasks: List[Task]) -> None:
    """Validate a list of tasks.

    Args:
        tasks: List of tasks to validate

    Raises:
        ValueError: If tasks list contains invalid data
    """
    if tasks and not all(isinstance(task, Task) for task in tasks):
        raise ValueError("All items must be Task objects")

    # Check for duplicate IDs only if list is not empty
    if tasks:
        task_ids = [task.id for task in tasks]
        if len(task_ids) != len(set(task_ids)):
            raise ValueError("Task list contains duplicate IDs")

# Usage example
try:
    validate_task_list(task_list)
    # Proceed with valid task list
except ValueError as e:
    print(f"Task validation failed: {e}")
    # Handle validation error
```

## Data Persistence

### File Storage Guidelines
- **Prefer JSON** for structured data
- **Consider CSV** for tabular data
- **Use plain text** for simple configurations
- **Handle file operations safely** with proper error handling

### Storage Implementation

#### Recommended Storage Pattern
```python
# storage.py example
import json
import os
from typing import List, Dict, Any

# File constants
TASKS_FILE = "tasks.json"
BACKUP_FILE = "tasks_backup.json"

def save_tasks(tasks: List[Dict[str, Any]]) -> None:
    """Save tasks to JSON file with backup.

    Args:
        tasks: List of tasks to save

    Raises:
        IOError: If file cannot be written
        Exception: For other unexpected errors
    """
    # Create backup of existing file
    if os.path.exists(TASKS_FILE):
        try:
            with open(TASKS_FILE, 'r') as source:
                with open(BACKUP_FILE, 'w') as backup:
                    backup.write(source.read())
        except Exception as e:
            print(f"Warning: Could not create backup: {e}")

    # Save current data
    try:
        with open(TASKS_FILE, 'w') as file:
            json.dump(tasks, file, indent=2)
    except Exception as e:
        raise IOError(f"Failed to save tasks: {e}")

def load_tasks() -> List[Dict[str, Any]]:
    """Load tasks from JSON file.

    Returns:
        List of tasks

    Raises:
        FileNotFoundError: If file doesn't exist
        ValueError: If file contains invalid data
        json.JSONDecodeError: If JSON is malformed
    """
    if not os.path.exists(TASKS_FILE):
        raise FileNotFoundError(f"Tasks file '{TASKS_FILE}' not found")

    try:
        with open(TASKS_FILE, 'r') as file:
            tasks = json.load(file)

        # Validate data structure
        if not isinstance(tasks, list):
            raise ValueError("Invalid tasks data format")

        return tasks

    except json.JSONDecodeError as e:
        print(f"Error: Tasks file is corrupted: {e}")
        print("Attempting to load backup...")
        return load_backup_tasks()
    except Exception as e:
        raise ValueError(f"Error loading tasks: {e}")

def load_backup_tasks() -> List[Dict[str, Any]]:
    """Load tasks from backup file.

    Returns:
        List of tasks from backup, or empty list if backup unavailable
    """
    try:
        if os.path.exists(BACKUP_FILE):
            with open(BACKUP_FILE, 'r') as file:
                return json.load(file)
        return []
    except Exception as e:
        print(f"Warning: Could not load backup: {e}")
        return []
```

#### Flexible Storage Usage
```python
# Example usage with proper error handling
try:
    tasks = load_tasks()
except FileNotFoundError:
    print("No existing tasks file found. Starting fresh.")
    tasks = []
except ValueError as e:
    print(f"Error loading tasks: {e}")
    print("Starting with empty task list.")
    tasks = []
except Exception as e:
    print(f"Unexpected error: {e}")
    # Decide whether to continue or exit based on application needs
    tasks = []

# Save tasks with error handling
try:
    save_tasks(tasks)
    print("Tasks saved successfully!")
except Exception as e:
    print(f"Error saving tasks: {e}")
    # Could retry, show warning, or exit depending on requirements
```

## CLI Menu Design

### Menu Structure Rules
- **Clear numbering**: Use sequential numbers for options
- **Descriptive labels**: Explain what each option does
- **Consistent formatting**: Align options neatly
- **Exit option**: Always include way to quit
- **Feedback**: Show what happened after each action

### Menu Implementation
```python
# main.py menu example
def show_main_menu() -> None:
    """Display the main menu and handle user input."""
    while True:
        print("\n" + "="*50)
        print("TASK MANAGER - MAIN MENU")
        print("="*50)
        print("1. View All Tasks")
        print("2. Add New Task")
        print("3. Update Task")
        print("4. Delete Task")
        print("5. Save Tasks to File")
        print("6. Load Tasks from File")
        print("7. Exit")
        print("="*50)

        try:
            choice = input("Enter your choice (1-7): ").strip()

            if choice == "1":
                view_all_tasks()
            elif choice == "2":
                add_new_task()
            elif choice == "3":
                update_task()
            elif choice == "4":
                delete_task()
            elif choice == "5":
                save_tasks_to_file()
            elif choice == "6":
                load_tasks_from_file()
            elif choice == "7":
                print("Goodbye! Thank you for using Task Manager.")
                break
            else:
                print("Invalid choice. Please enter a number between 1 and 7.")

        except KeyboardInterrupt:
            print("\nOperation cancelled by user.")
            break
        except Exception as e:
            print(f"An error occurred: {e}")
            print("Please try again.")
```

### Feedback Messages
- **Success**: "Task added successfully!"
- **Error**: "Error: Invalid input. Please try again."
- **Warning**: "Warning: No tasks found."
- **Confirmation**: "Are you sure you want to delete this task? (y/n): "

## Testing and Validation

### Testing Requirements
- **Test each function** individually
- **Test edge cases** (empty inputs, invalid data)
- **Test error conditions**
- **Verify data integrity** after operations

### Validation Checklist
```python
# Example test function
def test_task_creation():
    """Test task creation functionality."""
    print("Testing task creation...")

    # Test normal case
    task1 = create_task("Buy groceries", "Milk, eggs, bread")
    assert task1.title == "Buy groceries"
    assert task1.description == "Milk, eggs, bread"
    assert not task1.completed

    # Test empty description
    task2 = create_task("Do laundry")
    assert task2.title == "Do laundry"
    assert task2.description == ""

    # Test invalid title
    try:
        create_task("")
        assert False, "Should have raised ValueError"
    except ValueError:
        pass  # Expected

    print("✓ Task creation tests passed")

def run_all_tests():
    """Run comprehensive test suite."""
    print("Running tests...")

    test_task_creation()
    test_task_deletion()
    test_data_persistence()
    test_input_validation()

    print("All tests completed!")
```

## Beginner-Friendly Practices

### Code Readability Tips
- **Use whitespace** to separate logical sections
- **Limit line length** to 80-100 characters
- **Use consistent indentation** (4 spaces)
- **Avoid deep nesting** (use early returns)
- **Keep functions short** and focused

### Error Prevention
- **Initialize variables** before use
- **Check for None** values
- **Validate file operations**
- **Handle user interruptions** (Ctrl+C)
- **Use defensive programming**

### Debugging Help
- **Add debug prints** temporarily (remove before final)
- **Use meaningful variable names**
- **Write small, testable functions**
- **Check assumptions** with assertions

## Implementation Checklist

### Before Starting
- [ ] Read CLAUDE.md guidelines thoroughly
- [ ] Plan project structure
- [ ] Identify core functions needed
- [ ] Design data models

### During Development
- [ ] Follow naming conventions
- [ ] Add type hints to all functions
- [ ] Write line-by-line comments
- [ ] Implement error handling
- [ ] Add input validation
- [ ] Create clear menu system
- [ ] Implement data persistence
- [ ] Write comprehensive tests

### Before Completion
- [ ] Run all tests
- [ ] Check for unused imports
- [ ] Verify all functions have docstrings
- [ ] Test edge cases
- [ ] Clean up debug code
- [ ] Ensure consistent formatting
- [ ] Test complete workflow

### Final Checks
- [ ] Does the code follow all CLAUDE.md guidelines?
- [ ] Are all functions properly documented?
- [ ] Does error handling cover all cases?
- [ ] Is the menu system clear and user-friendly?
- [ ] Does data persistence work reliably?
- [ ] Have all tests passed?

## Additional Resources

### Recommended Patterns
```python
# Task class example
class Task:
    """Represents a task with title, description, and completion status."""

    def __init__(self, title: str, description: str = "", completed: bool = False):
        self.id = str(uuid.uuid4())
        self.title = self._validate_title(title)
        self.description = description
        self.completed = completed
        self.created_at = datetime.now()

    def _validate_title(self, title: str) -> str:
        """Validate task title."""
        if not title or title.strip() == "":
            raise ValueError("Task title cannot be empty")
        return title.strip()

    def mark_complete(self) -> None:
        """Mark task as completed."""
        self.completed = True

    def update(self, title: str = None, description: str = None) -> None:
        """Update task properties."""
        if title is not None:
            self.title = self._validate_title(title)
        if description is not None:
            self.description = description

    def to_dict(self) -> Dict[str, Any]:
        """Convert task to dictionary for serialization."""
        return {
            "id": self.id,
            "title": self.title,
            "description": self.description,
            "completed": self.completed,
            "created_at": self.created_at.isoformat()
        }

    @classmethod
    def from_dict(cls, data: Dict[str, Any]) -> 'Task':
        """Create task from dictionary."""
        task = cls(data["title"], data.get("description", ""))
        task.id = data["id"]
        task.completed = data.get("completed", False)
        task.created_at = datetime.fromisoformat(data["created_at"])
        return task
```

## Conclusion

This guide provides a comprehensive framework for building maintainable, beginner-friendly applications. Always refer to these guidelines when creating new projects to ensure consistency and quality.

**Remember**: The goal is to create code that is easy to understand, maintain, and extend - not to show off advanced programming skills.

Happy coding! 🚀