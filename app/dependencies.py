from fastapi import Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer
from jose import jwt, JWTError
from .schemas.user import user_schema
from .utils.search_user import search_user
from .utils.dot_env import SECRET_KEY, ALGORITHM


oAuth2 = OAuth2PasswordBearer(tokenUrl='/login')


async def auth_user(token:str = Depends(oAuth2)):
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        email = payload.get("email")
        user = search_user("email", email)
        if user is None:
            raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Invalid authentication credentials", headers={"WWW-Authenticate": "Bearer"})
        return user_schema(user)
    except JWTError as exc:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Invalid authentication credentials", headers={"WWW-Authenticate": "Bearer"}) from exc
