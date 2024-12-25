FROM python:3.11-slim

WORKDIR /app

COPY requirements.txt requirements.txt

RUN pip install -r requirements.txt && pip install "uvicorn[standard]"

CMD ["uvicorn", "app:app", "--reload", "--port", "2341", "--host", "0.0.0.0"] 