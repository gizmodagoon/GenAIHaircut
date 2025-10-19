from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from api.routes import haircuts

app = FastAPI(title="GenAI Haircut Tracker API", version="0.1")

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

@app.get("/")
def root():
    return {"message": "Welcome to the GenAI Haircut Tracker API!"}