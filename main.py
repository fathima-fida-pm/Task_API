from fastapi import FastAPI

from database import create_table

from routes import router


app = FastAPI(
    title="Task Management API",
    description="API for managing daily tasks",
    version="1.0"
)


@app.on_event("startup")
def startup():

    create_table()


app.include_router(router)


@app.get("/")
def home():

    return {
        "message": "Welcome to Task Management API"
    }