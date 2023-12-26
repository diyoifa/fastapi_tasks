def user_schema(user) -> dict:
    return {
        "id": str(user.get("_id")),
        "username": str(user.get("username")),
        "email": str(user.get("email")),
        "tasks": list(user["tasks"]),
    }