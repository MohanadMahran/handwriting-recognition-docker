
# Handwriting Recognition Docker

This project leverages a Python-based AI model to recognize handwritten numbers from images. The app is containerized using Docker to provide a consistent environment for running the app across different systems.

## Table of Contents
1. [Overview](#overview)
2. [Prerequisites](#prerequisites)
3. [Getting Started](#getting-started)
4. [Docker Setup](#docker-setup)
5. [Running the Application](#running-the-application)
6. [Project Structure](#project-structure)
7. [Requirements](#requirements)
8. [License](#license)

## Overview
This application uses Python and AI-based libraries to recognize handwritten digits. The image is uploaded via a web interface, sent to a pre-trained model, and the result is displayed back to the user. The entire application is built using Docker, making it easy to deploy in different environments.

## Prerequisites
Before you begin, ensure you have the following installed:

- **Docker**: [Install Docker](https://docs.docker.com/get-docker/)
- **Docker Compose**: [Install Docker Compose](https://docs.docker.com/compose/install/)
- **Python (for local testing or development)**: [Download Python](https://www.python.org/downloads/)

## Getting Started
To get started with this project, follow the steps below:

### Clone the repository to your local machine:
```bash
git clone https://github.com/yourusername/handwriting-recognition-docker.git
cd handwriting-recognition-docker
```

### Create and activate a virtual environment (optional, for local testing):
```bash
python -m venv venv
source venv/bin/activate  # On Windows use 'venv\Scripts\activate'
```

### Install dependencies:
```bash
pip install -r requirements.txt
```

## Docker Setup
This project is designed to run inside a Docker container. To set up the Docker environment, ensure you have Docker and Docker Compose installed on your system.

### Build the Docker image:
```bash
docker build -t handwriting-recognition .
```

### Start the application with Docker Compose:
```bash
docker-compose up
```

This will start the application inside a Docker container. Once the services are up and running, you can access the web interface through [http://localhost:5000](http://localhost:5000).

## Running the Application
If you want to run the application locally without Docker, you can do so by running the following command:

```bash
python app.py
```

This will start a local development server on [http://localhost:5000](http://localhost:5000), and you can interact with the web interface.

## Project Structure
The directory structure of the project looks like this:

```
handwriting-recognition-docker/
├── app.py                 # Main Flask application
├── model.py               # Script to train and save the model
├── handwriting_model.h5   # Pre-trained model file (generated after running `model.py`)
├── requirements.txt       # List of dependencies with specific versions
├── Dockerfile             # Docker instructions
├── docker-compose.yml     # Docker Compose file for service management
└── templates/
    └── index.html         # HTML file for image upload interface
```

### Description of Key Files:
- `app.py`: Contains the Flask web application where images are uploaded, processed, and results are returned.
- `model.py`: Script to train the AI model. This script should be run to generate the pre-trained model (`handwriting_model.h5`).
- `handwriting_model.h5`: The pre-trained model file that is used by the Flask app to predict handwritten numbers.
- `requirements.txt`: Specifies the Python dependencies needed to run the application.
- `Dockerfile`: Contains the Docker instructions to containerize the app.
- `docker-compose.yml`: Defines the services and configuration for running the app with Docker Compose.
- `templates/index.html`: Simple HTML interface for users to upload images for recognition.

## Requirements
The project relies on the following Python libraries and dependencies:

- Flask
- TensorFlow
- Keras
- NumPy
- Pillow

You can find the full list in the `requirements.txt` file, and make sure to install all dependencies with:

```bash
pip install -r requirements.txt
```

## License
This project is licensed under the MIT License - see the LICENSE file for details.

---
