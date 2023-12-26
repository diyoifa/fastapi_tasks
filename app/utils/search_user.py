from ..config.db import client
from fastapi import status, HTTPException
from ..models.user import User
from ..schemas.user import user_schema

def search_user(key: str, value):
    try:
        user = client.users.find_one({key: value})
        if user == None:
            return None
        return user
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=str(e))
    

