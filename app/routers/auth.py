from jose import jwt
from fastapi import APIRouter, HTTPException, status
from fastapi.security import OAuth2PasswordBearer
from ..schemas.user import user_schema
from ..models.user import Credentials
from ..utils.search_user import search_user
from ..utils.crypt import check_password
from ..utils.dot_env import SECRET_KEY, ALGORITHM


oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/login")
# crypt = CryptContext(schemes=["bcrypt"])

router = APIRouter(
    prefix="/login",
    tags=["Auth"],
    responses={status.HTTP_404_NOT_FOUND: {"description": "Not found"}},
)


@router.post("/", status_code = status.HTTP_200_OK)
async def login(user: Credentials):
    user_db = search_user("email", user.email)
    if user_db is None or  check_password(user.password, user_db["password"]) is False:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Invalid credentials")
    user_dict = {"id":str(user_db["_id"]), "email": user_db["email"]}
    token = jwt.encode(user_dict, SECRET_KEY, algorithm=ALGORITHM)
    return {"access_token": token, "user": user_schema(user_db), "token_type": "bearer"}


