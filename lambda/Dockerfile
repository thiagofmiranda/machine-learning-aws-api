# Use the base image for AWS Lambda with Python 3.11 runtime
FROM public.ecr.aws/lambda/python:3.11

# Copy the main requirements file to the Lambda task root directory
COPY requirements.txt ${LAMBDA_TASK_ROOT}

# Install the main dependencies listed in requirements.txt
RUN pip install -r requirements.txt

# Copy the main API codes to the Lambda task root directory
COPY src/routes.py ${LAMBDA_TASK_ROOT}/routes.py
COPY src/app.py ${LAMBDA_TASK_ROOT}/app.py

# Copy the machine learning models to the appropriate directory in the container
COPY src/machine-learning-models/models ${LAMBDA_TASK_ROOT}/models

# Install dependencies for each model if a requirements.txt exists in its folder
RUN find ${LAMBDA_TASK_ROOT}/models -type f -name 'requirements.txt' -exec pip install -r {} \;

# Define the command to start the Lambda function, specifying the handler method
CMD [ "app.handler" ]
