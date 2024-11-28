from fastapi import FastAPI
from routes import router
from mangum import Mangum
from pydantic import BaseModel

# Initialize the FastAPI app
app = FastAPI()
handler = Mangum(app)

# Include dynamically created routes
app.include_router(router)