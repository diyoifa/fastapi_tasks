from .search_user import search_user
from fastapi import status, HTTPException
from .crypt import encrypt_password
from ..models.user import User

def user_to_dict(user: User):
        try:
                # user_db = search_user("email", user.email)
                # print(user_db)
                password_hash = encrypt_password(user.password)
                print(password_hash)
                user.password = password_hash
                user_dict = dict(user)
                del user_dict["id"]
                return user_dict
        except Exception as e:
                raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=str(e))