FROM python:3.11

ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1 \
    PYTHONIOENCODING=utf-8

RUN apt-get update && \
    apt-get install -y curl \
    && rm -rf /var/lib/apt/lists/* \
    apt-get clean

WORKDIR /app
VOLUME [ "/app" ]
COPY . .

WORKDIR /app
ENV PYTHONPATH=${PYTHONPATH}:${PWD}
RUN pip3 install poetry \
    && poetry config virtualenvs.create false \
    && poetry install --no-dev


CMD ["poetry", "run", "uvicorn", "app.main:app", "--host", "0.0.0.0", "--reload"]
