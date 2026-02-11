from fastapi import FastAPI
from app.routers import projects

app = FastAPI(
    title="ProjetAPI",
    description="API de gestion des projets étudiants",
    version="1.0.0",
)

x = 1


@app.get("/")
def read_root():
    return {"message": "Bienvenue dans ProjetAPI"}


app.include_router(projects.router)
