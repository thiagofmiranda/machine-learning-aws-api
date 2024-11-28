## Project Description

This project aims to create a Python API using FastAPI and deploy it to AWS using AWS Lambda. The application is containerized using Docker to provide an isolated and reproducible development environment. AWS SAM CLI is utilized for local testing, building, and deploying the serverless application to AWS. The project demonstrates how to efficiently build and deploy a scalable API with FastAPI on AWS Lambda, leveraging the simplicity and flexibility of Docker and AWS serverless services.

## Requirements

### Docker

Follow the installation steps for Docker in this [link](https://docs.docker.com/engine/install/).

### AWS CLI

Follow the installation steps for the AWS CLI in this [link](https://docs.aws.amazon.com/cli/latest/userguide/getting-started-install.html).

Configure AWS CLI by running:
```bash
aws configure
```

### AWS SAM CLI

Follow the installation steps for AWS SAM CLI in this [link](https://docs.aws.amazon.com/serverless-application-model/latest/developerguide/install-sam-cli.html).

Verify the installation with:
```bash
sam --version
```

### Local Testing with AWS SAM CLI

To test locally using AWS SAM CLI:

1. Build the application:
   ```bash
   sam build
   ```

2. Start the local API:
   ```bash
   sam local start-api
   ```

3. Test the local endpoints:
   ```bash
   curl http://localhost:3000/hc
   curl http://localhost:3000/list-models
   ```

### Deployment

To deploy the application:

1. Deploy using AWS SAM CLI:
   ```bash
   sam deploy --guided
   ```

2. Test in the AWS dev stage with:
   ```bash
   curl https://yfb41zsxa9.execute-api.us-east-1.amazonaws.com/dev/hc
   curl https://yfb41zsxa9.execute-api.us-east-1.amazonaws.com/dev/list-models
   ```