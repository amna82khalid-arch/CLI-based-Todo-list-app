from datetime import datetime
from typing import List, Dict, Any, Optional, Literal

# Allowed status values
TaskStatus = Literal["pending", "in-progress", "completed"]
ALLOWED_STATUSES = ["pending", "in-progress", "completed"]

class Task:
    """Represents a single todo task."""

    def __init__(
        self,
        title: str,
        status: TaskStatus = "pending",
        completed: bool = False,
        task_id: Optional[str] = None,
        due_date: Optional[str] = None,
        reminder_time: Optional[str] = None,
        completed_at: Optional[str] = None
    ):
        # Use provided ID for loading from storage, or generate sequential numeric ID
        if task_id:
            # For loading from storage, validate it's a valid numeric ID
            try:
                int(task_id)  # Validate it's numeric
                self.id = task_id
            except ValueError:
                # If invalid, generate a new numeric ID (will be set later)
                self.id = None
        else:
            # For new tasks, we'll set the ID later after we know existing tasks
            self.id = None  # Will be set by set_task_id method

        # Validate title with a safe default if invalid
        self.title = self._validate_title(title)
        # Validate status with a safe default if invalid
        self.status = self._validate_status(status)
        # Sync completed boolean with status
        self.completed = completed or (self.status == "completed")
        self.created_at = datetime.now().isoformat()

        # Optional fields
        self.due_date = due_date
        self.reminder_time = reminder_time
        self.completed_at = completed_at

        # Ensure completed_at is set if task is initialized as completed
        if self.completed and not self.completed_at:
            self.completed_at = datetime.now().isoformat()

    def set_task_id(self, task_id: int) -> None:
        """Set the task ID to a numeric value.

        Args:
            task_id: Integer ID for the task
        """
        self.id = str(task_id)

    def _validate_title(self, title: Optional[str]) -> str:
        """Validate title and return default if invalid."""
        if not title or not isinstance(title, str):
            return "Untitled Task"

        cleaned = title.strip()
        return cleaned if cleaned else "Untitled Task"

    def _validate_status(self, status: Any) -> TaskStatus:
        """Validate status value and return default 'pending' if invalid."""
        if status in ALLOWED_STATUSES:
            return status
        return "pending"

    def mark_completed(self) -> None:
        """Mark the task as completed and update status and timestamp."""
        self.completed = True
        self.status = "completed"
        self.completed_at = datetime.now().isoformat()

    def update_status(self, new_status: str) -> None:
        """Update task status with validation and sync completed state."""
        self.status = self._validate_status(new_status)
        if self.status == "completed":
            self.completed = True
            if not self.completed_at:
                self.completed_at = datetime.now().isoformat()
        else:
            self.completed = False
            self.completed_at = None

    def update_title(self, new_title: str) -> None:
        """Update task title with validation."""
        self.title = self._validate_title(new_title)

    def set_due_date(self, due_date: Optional[str]) -> None:
        """Update the due date."""
        self.due_date = due_date

    def set_reminder_time(self, reminder_time: Optional[str]) -> None:
        """Update the reminder time."""
        self.reminder_time = reminder_time

    def to_dict(self) -> Dict[str, Any]:
        """Convert task to dictionary for storage."""
        return {
            "id": self.id,
            "title": self.title,
            "status": self.status,
            "completed": self.completed,
            "created_at": self.created_at,
            "due_date": self.due_date,
            "reminder_time": self.reminder_time,
            "completed_at": self.completed_at
        }

    @classmethod
    def from_dict(cls, data: Dict[str, Any]) -> 'Task':
        """Create a Task object from a dictionary."""
        # Use safe defaults for missing dictionary keys
        task = cls(
            title=data.get("title", "Untitled Task"),
            status=data.get("status", "pending"),
            completed=data.get("completed", False),
            task_id=data.get("id"),
            due_date=data.get("due_date"),
            reminder_time=data.get("reminder_time"),
            completed_at=data.get("completed_at")
        )
        task.created_at = data.get("created_at", datetime.now().isoformat())
        return task

def get_next_task_id(existing_tasks: List[Task]) -> int:
    """Get the next available numeric task ID.

    Args:
        existing_tasks: List of existing tasks to check for ID conflicts

    Returns:
        Next available integer ID (starting from 1)
    """
    if not existing_tasks:
        return 1

    # Get all existing numeric IDs and find the highest
    numeric_ids = []
    for task in existing_tasks:
        try:
            # Convert ID to integer (all IDs should be numeric now)
            numeric_id = int(task.id)
            numeric_ids.append(numeric_id)
        except (ValueError, TypeError):
            # This should not happen in pure numeric system, but handle gracefully
            continue

    # Return next ID after the highest found
    if numeric_ids:
        return max(numeric_ids) + 1
    else:
        return 1

# --- Core Task Operations ---

def add_task(
    tasks: List[Task],
    title: str,
    status: str = "pending",
    due_date: Optional[str] = None,
    reminder_time: Optional[str] = None
) -> List[Task]:
    """Add a new task with optional fields to the list."""
    # Create task without ID first
    new_task = Task(title, status=status, due_date=due_date, reminder_time=reminder_time)

    # Get next available numeric ID
    next_id = get_next_task_id(tasks)
    new_task.set_task_id(next_id)

    tasks.append(new_task)
    return tasks

def find_task_by_id(tasks: List[Task], task_id: str) -> Optional[Task]:
    """Search for a task by ID, returning None if not found."""
    for task in tasks:
        if task.id == task_id:
            return task
    return None

def delete_task(tasks: List[Task], task_id: str) -> List[Task]:
    """Remove a task from the list and return updated list."""
    return [t for t in tasks if t.id != task_id]

# --- Filtering and Search Functions ---

def get_pending_tasks(tasks: List[Task]) -> List[Task]:
    """Return only tasks that are currently pending. Handles empty lists gracefully."""
    if not tasks:
        return []
    return [t for t in tasks if t.status == "pending"]

def get_in_progress_tasks(tasks: List[Task]) -> List[Task]:
    """Return only tasks that are currently in progress. Handles empty lists gracefully."""
    if not tasks:
        return []
    return [t for t in tasks if t.status == "in-progress"]

def get_completed_tasks(tasks: List[Task]) -> List[Task]:
    """Return only tasks that are completed. Handles empty lists gracefully."""
    if not tasks:
        return []
    return [t for t in tasks if t.status == "completed"]

def search_tasks(tasks: List[Task], keyword: str) -> List[Task]:
    """Search tasks by title keyword (case-insensitive)."""
    if not tasks or not keyword or not isinstance(keyword, str):
        return []

    keyword_lower = keyword.lower().strip()
    if not keyword_lower:
        return []

    return [t for t in tasks if keyword_lower in t.title.lower()]
