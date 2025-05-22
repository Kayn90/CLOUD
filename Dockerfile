FROM python:3.10

WORKDIR /app
COPY . .

RUN pip install --upgrade pip && pip install -r requirements.txt
RUN playwright install --with-deps

CMD ["python", "club_selector.py"]
