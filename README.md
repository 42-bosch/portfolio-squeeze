# desafio_bosch_1

## Summary

- [Description](#description)
- [Requirements](#Requirements)
- [User](#User)

## Description

This is a straightforward REST API built using FastAPI and SQLAlchemy for the database, all packaged within Docker.

## requirements

- python 3.11
- pip
- docker
- docker-compose

## User

### run in docker

You have to change .env.sample to .env and add values to them

```bash
docker-compose up -d --build
```

### Run in local

You need to have a postgres database running on port 5432, and create environment variables

```bash
export POSTGRES_USER=#your user
export POSTGRES_PASSWORD=#your password
export POSTGRES_SERVER=localhost
export POSTGRES_PORT=5432
export POSTGRES_DB=#your database
```

if you not have ambiente virtual, you can create with this commands

```bash
pip -m venv venv
```

```bash
source venv/bin/activate
```

```bash
pip install -r requirements.txt
```

```bash
uvicorn main:app --reload
```
