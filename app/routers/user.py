from fastapi import APIRouter, status, HTTPException
from ..models.user import User
from ..schemas.user import user_schema
from ..config.db import client
from ..utils.search_user import search_user
# from ..utils.crypt import encrypt_password
from ..utils.user_to_dict import user_to_dict

router = APIRouter(
    prefix="/user",
    tags=["User"],
    responses={status.HTTP_404_NOT_FOUND: {"description": "Not found"}},
)

@router.get("/", status_code=status.HTTP_200_OK)
async def get_user():
    return {"message": "Hello World"}

@router.post('/register', status_code=status.HTTP_201_CREATED, response_description="User created successfully")
async def register(user: User):
    user_db = search_user("email", user.email)
    if user_db != None:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="User already registered")
    
    user_dict = user_to_dict(user)
    id = client.users.insert_one(user_dict)
    new_user = user_schema(client.users.find_one({"_id": id.inserted_id}))
    print(new_user)
    return new_user
