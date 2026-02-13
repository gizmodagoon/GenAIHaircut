from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from api.routes import haircuts, barbers
from contextlib import asynccontextmanager
from fastapi import FastAPI
from db.db import engine, Base

@asynccontextmanager
async def lifespan(app: FastAPI):
    # STARTUP
    print("Starting DB...")
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)

    yield

    # SHUTDOWN
    print("Closing DB...")
    await engine.dispose()

app = FastAPI(title="GenAI Haircut Tracker API", version="0.1", lifespan=lifespan)

# CORS configuration
origins = [
    "http://localhost:5173",  # Vite frontend dev server
    # Add production frontend URL later
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,       # allowed domains
    allow_credentials=True,
    allow_methods=["*"],         # GET, POST, etc.
    allow_headers=["*"],
)

# Include routes
app.include_router(haircuts.router)
app.include_router(barbers.router)

@app.get("/")
def root():
    return {"message": "Welcome to the GenAI Haircut Tracker API!"}