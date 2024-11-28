
## Requirements

### Docker

The Docker installation steps is in this (link)[https://docs.docker.com/engine/install/]


### AWS CLI

The AWS cli installation steps is in this (link)[https://docs.aws.amazon.com/cli/latest/userguide/getting-started-install.html]

Configure: 
```bash
aws configure
```

### AWS SAM CLI

The Zip installation steps is in this (link)[https://docs.aws.amazon.com/serverless-application-model/latest/developerguide/install-sam-cli.html]

Verify the instalation
```bash
sam --version
```


### Local test
Testing locally using AWS SAM CLI

Running:  
```bash
sam build
sam local start-api
```

Testing:
```bash
curl http://localhost:3000/hc
curl http://localhost:3000/list-models
```

### Local test
Testing locally using AWS SAM CLI

Running:  
```bash
sam build --template-file tests/template.yaml
sam local start-api
```

Testing:
```bash
curl http://localhost:3000/list-models
```
