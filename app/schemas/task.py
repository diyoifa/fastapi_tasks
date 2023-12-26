def task_schema(task) -> dict:
    return {
        "id": str(task["_id"]),
        "title": str(task["title"]),
        "description": str(task["description"]),
        "completed": bool(task["completed"]),
    }

def tasks_schema(tasks) -> list:
    return [task_schema(task) for task in tasks]