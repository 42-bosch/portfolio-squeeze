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

### run in local

```bash
pip install -r requirements.txt
```

```bash
uvicorn main:app --reload
```

