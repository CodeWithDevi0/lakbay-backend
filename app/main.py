from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.database.session import engine, Base
from app.routers import auth

# Create database tables
Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="Lakbay API",
    description="Backend API for Lakbay",
    version="1.0.0"
)

# Configure CORS for local frontend development (Vue connects typically to 5173 or 3000)
origins = [
    "http://localhost:5173",  # Vite default port
    "http://localhost:3000",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Include routers
app.include_router(auth.router)

@app.get("/", include_in_schema=False)
def read_root():
    return {"message": "Welcome to Lakbay API"}
