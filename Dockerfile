FROM python:3.10

WORKDIR /app
COPY . .

RUN pip install --upgrade pip && pip install -r requirements.txt
RUN playwright install --with-deps

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "80"]
