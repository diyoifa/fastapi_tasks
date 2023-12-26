from pydantic import BaseModel
from typing import Optional, List
# from .task import Task  # Importar Task después de que User esté definido

class User(BaseModel):
    id: Optional[str] = None
    username: str
    email: str
    password: Optional[str] = None
    tasks: Optional[list] = []

class Credentials(BaseModel):
    email: str
    password: str

