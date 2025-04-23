# Simple ML Model Deployment

This project demonstrates a simple machine learning model deployment using Flask, Docker, and AWS.

## Project Overview

This project deploys a pre-trained Iris flower classifier as a RESTful API with the following components:

- Machine Learning model: RandomForest classifier trained on the Iris dataset
- API: Flask-based REST API for serving predictions
- Container: Docker container packaging the API and model
- CI/CD: GitHub Actions workflow for automated testing and deployment
- Cloud: AWS EC2 for hosting the containerized application
- API Gateway: AWS API Gateway for secure API exposure

## Project Structure

```
simple-ml-model-deployment/
├── .github/
│   └── workflows/
│       └── main.yml       # GitHub Actions workflow
├── app/
│   ├── __init__.py
│   ├── main.py            # Flask API
│   └── model.py           # ML model implementation
├── tests/
│   ├── __init__.py
│   └── test_model.py      # Model tests
├── Dockerfile             # Docker container definition
├── requirements.txt       # Python dependencies
└── README.md              # Project documentation
```

## API Endpoints

- `GET /`: API information
- `POST /predict`: Make a prediction
  - Request body: `{"features": [sepal_length, sepal_width, petal_length, petal_width]}`
  - Response: `{"prediction": class_id, "species": species_name}`

## Deployment Steps

1. Create a GitHub repository and push all the code
2. Set up the following GitHub secrets:
   - `DOCKER_HUB_USERNAME`: Your Docker Hub username
   - `DOCKER_HUB_ACCESS_TOKEN`: Your Docker Hub access token
   - `EC2_HOST`: Your AWS EC2 instance IP
   - `EC2_USERNAME`: Your EC2 instance username (e.g., `ec2-user`)
   - `EC2_SSH_KEY`: Your EC2 SSH private key
3. Push to the main branch to trigger the GitHub Actions workflow
4. The workflow will:
   - Run tests
   - Build and push the Docker image to Docker Hub
   - Deploy the container to AWS EC2

## AWS EC2 Setup

1. Launch an EC2 instance with Amazon Linux 2
2. Install Docker:
   ```bash
   sudo yum update -y
   sudo amazon-linux-extras install docker -y
   sudo service docker start
   sudo usermod -a -G docker ec2-user
   ```
3. Set up an API Gateway to securely expose the API

## Local Development

1. Clone the repository
2. Install dependencies: `pip install -r requirements.txt`
3. Run tests: `pytest`
4. Run the application: `python -m app.main`
5. Access the API at http://localhost:5000
