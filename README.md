# External API Layer with FastAPI and Docker

This repository contains a simple implementation of an external API layer using FastAPI wrapped in a Docker container. The primary objective of this project is to demonstrate how to add an extra layer of security by creating an intermediary API for calling internal APIs.
## Features
- **FastAPI:** Utilizes FastAPI, a modern web framework for building APIs with Python. FastAPI provides high performance and automatic documentation generation.
- **Docker:** Containerizes the FastAPI application, ensuring consistency across different environments and facilitating deployment.
- **External API Layer:** Demonstrates the implementation of an external API layer, enhancing security measures by providing a controlled interface for accessing flask based internal APIs.

## Technologies Used
- **Backend:** FastApi, Docker.
- **API:** Flask Internal Apis.

## Installation
1. Clone this repository to your local machine.
2. Install the necessary dependencies using `pip install -r requirements.txt`.

## Usage
1. Run the Flask application using `python app.py`.
