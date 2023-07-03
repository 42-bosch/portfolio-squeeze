FROM tiangolo/uvicorn-gunicorn-fastapi:python3.11

ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1 \
    PYTHONIOENCODING=utf-8

RUN apt-get update && \
    apt-get install -y curl \
    && rm -rf /var/lib/apt/lists/* \
    apt-get clean

WORKDIR /app
COPY requirements.txt .
COPY . .

RUN pip install -r requirements.txt

CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--reload"]
