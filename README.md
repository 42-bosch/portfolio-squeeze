# Project Portfolio Squeeze

![Project Logo](https://fastapi.tiangolo.com/img/logo-margin/logo-teal.png)

## Summary

- [Description](#description)
- [Requirements](#requirements)
- [Usage](#usage)
- [API Documentation](#api-documentation)

## Description

Project Portfolio Squeeze is a straightforward REST API built using FastAPI and SQLAlchemy for the database, all packaged within Docker. It provides a simple and efficient way to create, read, update, and delete data through API endpoints.

## Features

This project includes the following features:

- [x] Creation of a REST API using FastAPI
- [x] Use of a relational database
- [x] Dockerized application for easy deployment and scalability
- [ ] Utilization of a testing library

## Requirements

To run Project Portfolio Squeeze, you need to have the following requirements:

- Docker
- Docker Compose

**Note:** All other requirements are installed inside the Docker containers.

## Usage

Follow the steps below to run Project Portfolio Squeeze using Docker:

1. Rename the file `.env.sample` to `.env` and update the values accordingly.

    **Note:** To generate the secret key, you can use the following command:

    ```bash
    openssl rand -hex 32 # for Linux and Mac

    # Or go to https://generate-random.org/encryption-key-generator
    # and generate a key with 32 characters
    ```

2. Open a terminal or command prompt and navigate to the project directory.

3. Run the following command to build and start the Docker containers:

```bash
docker-compose up # or docker compose up -d
```

4. Once the containers are up and running, you can access the API endpoints using the provided URLs.

## API Documentation

To access the API documentation, open a browser and navigate to the following URL:

```bash
http://localhost:8000/docs # for Swagger UI
```

**Note:** By default, the backend is running on port 8000.

## Contributing

Contributions are welcome! If you find any issues or have suggestions for improvements, please open an issue or submit a pull request.

## License

This project is licensed under the [MIT License](LICENSE).

## Acknowledgments

- [FastAPI Documentation](https://fastapi.tiangolo.com/)
- [Docker Documentation](https://docs.docker.com/)
- [SQLAlchemy Documentation](https://docs.sqlalchemy.org/)
- [pgAdmin Documentation](https://www.pgadmin.org/docs/)
