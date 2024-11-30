from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from routes import router
from mangum import Mangum
from pydantic import BaseModel

# Initialize the FastAPI app
app = FastAPI()

# Configure CORS middleware
origins = ["*"]  
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,  
    allow_credentials=True,  
    allow_methods=["*"], 
    allow_headers=["*"],  
)

# Include dynamically created routes
app.include_router(router)

# Lambda handler for API Gateway integration
handler = Mangum(app)