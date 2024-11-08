FROM python:3.12-slim

ENV PYTHONUNBUFFERED=1 \
    PYTHONDONTWRITEBYTECODE=1

WORKDIR /usr/src/app

COPY requirements.txt ./
COPY .env ./

RUN pip install --no-cache-dir -r requirements.txt

COPY post_service ./post_service

CMD ["uvicorn", "post_service.main:app", "--host", "0.0.0.0", "--port", "8001"]