from fastapi import APIRouter
from app.models import Project
from app.utils.db_manager import read_db, write_db

router = APIRouter(prefix="/projects", tags=["Projects"])


@router.post("/")
def create_project(project: Project):
    db = read_db()

    db["projects"].append(project.dict())

    write_db(db)

    return {"message": "Projet créé avec succès", "project": project}


@router.get("/")
def get_projects():
    db = read_db()
    return db["projects"]
