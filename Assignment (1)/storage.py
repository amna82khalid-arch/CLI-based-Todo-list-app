import json
import os
from typing import List, Dict, Any

# File constant
TASKS_FILE = "tasks.json"

def save_tasks(tasks: List[Dict[str, Any]]) -> None:
    """Save tasks to JSON file.

    Args:
        tasks: List of task dictionaries to save
    """
    # Attempt to save current data, failing silently if error occurs
    try:
        with open(TASKS_FILE, 'w') as file:
            json.dump(tasks, file, indent=2)
    except Exception:
        # Silently fail as per CLAUDE.md guidance for non-critical operations
        pass

def load_tasks() -> List[Dict[str, Any]]:
    """Load tasks from JSON file.

    Returns:
        List of tasks or empty list if file missing or corrupted
    """
    # Return default empty list if file doesn't exist
    if not os.path.exists(TASKS_FILE):
        return []

    # Attempt to load and parse JSON content
    try:
        with open(TASKS_FILE, 'r') as file:
            data = json.load(file)

        # Ensure data is the expected list format
        if isinstance(data, list):
            return data
        return []
    except (json.JSONDecodeError, Exception):
        # Return safe default empty list on any error
        return []
