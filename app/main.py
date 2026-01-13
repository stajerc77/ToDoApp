from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session
from .database import engine, SessionLocal, Base
from .models import Task


# Create tables
Base.metadata.create_all(bind=engine)

app = FastAPI(title="ToDoApp API", description="App to structure everyday tasks")

# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.get("/")
async def root(db: Session = Depends(get_db)):
    return {"message": "🎉 FastAPI ToDo App Working!", "status": "ready"}
