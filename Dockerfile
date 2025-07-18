
FROM python:3.10-slim


WORKDIR /app


COPY . .


RUN pip install --no-cache-dir -r requirements.txt


EXPOSE 8000
EXPOSE 5000


CMD ["bash", "-c", "mlflow ui --port 5000 & uvicorn main:app --host 0.0.0.0 --port 8000"]
