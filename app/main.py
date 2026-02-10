from fastapi import FastAPI
from app.routers import projects

app = FastAPI(
    title="ProjetAPI",
    description="API de gestion des projets étudiants",
    version="1.0.0",
)


@app.get("/")
def read_root():
    return {"message": "Bienvenue dans ProjetAPI"}


x = 1

app.include_router(projects.router)
