from fastapi import FastAPI
from contextlib import asynccontextmanager
from src.db.main import init_db
from src.db.routes import router  # ✅ Import the router

@asynccontextmanager
async def lifespan(app: FastAPI):
    #things to do before starting the app
    print("Starting app")
    await init_db()
    yield
    #things to do before stopping the app and after the server has stopped
    print("Stopping app")

app = FastAPI(
    title="LB_V1.2",
    version="1.0.0", 
    description="This is a simple API to test the FastAPI framework",
    lifespan= lifespan
)


app.include_router(router, prefix="/api", tags=["Intervention Sessions"])
