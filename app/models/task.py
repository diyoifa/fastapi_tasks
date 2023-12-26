from pydantic import BaseModel
from typing import Optional, ForwardRef

class Task(BaseModel):
    id: Optional[str] = None
    title: str
    description: str
    completed: bool = False
