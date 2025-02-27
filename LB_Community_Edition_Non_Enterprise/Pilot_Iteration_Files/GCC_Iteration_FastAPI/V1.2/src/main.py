from fastapi import FastAPI
from src.db.main import init_db  # Import the function from src/db/main.py

app = FastAPI()

@app.get("/")
async def read_root():
    return {"message": "Hello World"}

@app.lifespan("startup")
async def startup_event():
    await init_db()  # Initialize the database connection at startup
