import os
import importlib
from fastapi import APIRouter
from pydantic import BaseModel


class PredictionRequest(BaseModel):
    input_data: dict


# Initialize the API Router
router = APIRouter()


# Base path to the models folder
MODELS_PACKAGE = "models"  # Base package name for the models folder
MODELS_PATH = os.path.join(os.path.dirname(os.path.abspath(__file__)), MODELS_PACKAGE)


# Store available models for use in the API
available_models = []

# Dynamically load predict functions from each model
for model_dir in os.listdir(MODELS_PATH):
    model_path = os.path.join(MODELS_PATH, model_dir)

    # Check if the directory contains an __init__.py file
    if os.path.isdir(model_path) and os.path.exists(os.path.join(model_path, "__init__.py")):
        # Add the model name to the list of available models
        available_models.append(model_dir)

        # Import the predict function dynamically
        module_name = f"{MODELS_PACKAGE}.{model_dir}.predict"
        try:
            predict_module = importlib.import_module(module_name)
            predict_function = getattr(predict_module, "predict")

            # Define a route for the model
            @router.post(f"/{model_dir}/predict")
            async def predict_endpoint(data: PredictionRequest):
                """
                Route for making predictions using the specific model.
                """
                prediction = predict_function(data.input_data)
                return {"prediction": prediction}

        except (ModuleNotFoundError, AttributeError) as e:
            print(f"Error loading predict function for model {model_dir}: {e}")


# Health Check Route
@router.get("/hc", tags=["Utility"])
async def health_check():
    """
    Health check endpoint to verify the API is running.
    """
    return {"status": "ok"}


# List Available Models Route
@router.get("/list-models", tags=["Utility"])
async def list_models():
    """
    List all available machine learning models.
    """
    return {"available_models": available_models}
