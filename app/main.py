from fastapi import FastAPI

app = FastAPI(title="Todo API", description="Portfolio project")

@app.get("/")
async def root():
    return {"message": "🎉 FastAPI Todo App Working!", "status": "ready"}

@app.get("/health")
async def health():
    return {"status": "healthy"}
