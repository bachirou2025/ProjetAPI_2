from pydantic import BaseModel
from typing import Optional


class Project(BaseModel):
    id: int
    title: str
    student_name: str
    course: str
    description: Optional[str] = None
    grade: Optional[float] = None
