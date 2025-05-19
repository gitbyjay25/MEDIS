from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from .database.db_config import engine, Base
from .auth.routes import router as auth_router
from .app import router as prediction_router

# Create database tables
Base.metadata.create_all(bind=engine)

# Create FastAPI app
app = FastAPI(title="MEDIS API")

# Configure CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # In production, replace with specific origins
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Include routers
app.include_router(auth_router, prefix="/auth", tags=["Authentication"])
app.include_router(prediction_router, prefix="/api", tags=["Prediction"])

@app.get("/")
async def root():
    return {"message": "Welcome to MEDIS API"} 