from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import FileResponse
from . import models
from .database import engine
from .routers import post, user, auth, vote
from .config import settings

# Create the FastAPI app
app = FastAPI(title="fastapi")
              
favicon_path = 'favicon.ico'
@app.get('/favicon.ico', include_in_schema=False)
async def favicon():
    return FileResponse(favicon_path)

# Configure CORS (Cross-Origin Resource Sharing) middleware
origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Include routers for different endpoints
app.include_router(post.router)
app.include_router(user.router)
app.include_router(auth.router)
app.include_router(vote.router)

# Define the root route
@app.get("/")
def root():
    """Root endpoint returning a greeting message."""
    return {"message": "Hello there!"}
