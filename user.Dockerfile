FROM python:3.12-slim

ENV PYTHONUNBUFFERED=1 \
    PYTHONDONTWRITEBYTECODE=1

WORKDIR /usr/src/app

COPY requirements.txt ./
COPY .env ./

RUN pip install --no-cache-dir -r requirements.txt

COPY user_service ./user_service

CMD ["uvicorn", "user_service.main:app", "--host", "0.0.0.0", "--port", "8000"]