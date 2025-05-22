FROM python:3.10-slim

RUN pip install fastapi uvicorn playwright
RUN playwright install

COPY . /app
WORKDIR /app

CMD ["sh", "-c", "uvicorn main:app --host 0.0.0.0 --port ${PORT:-8000}"]
