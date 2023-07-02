# Challenge_Bosch_1

## Summary

- [Description](#description)
- [Requirements](#requirements)
- [Usage](#usage)
- [User](#user)

## Description

The Challenge_Bosch_1 is a straightforward REST API built using FastAPI and SQLAlchemy for the database, all packaged within Docker. It provides a simple and efficient way to create, read, update, and delete data through API endpoints.

## Requirements

To run the Challenge_Bosch_1, you need the following requirements:

- Python 3.11
- Pip
- Docker
- Docker Compose

## Usage

Follow the steps below to run the Challenge_Bosch_1 in Docker:

1. Rename the file `.env.sample` to `.env` and update the values accordingly.

2. Open a terminal or command prompt and navigate to the project directory.

3. Run the following command to build and start the Docker containers:

```bash
docker-compose up -d --build
```

4. Once the containers are up and running, you can access the API endpoints using the provided URLs.

## User

Using a browser access the following URL to access the API documentation:

```bash
http://localhost:8080/docs
```
