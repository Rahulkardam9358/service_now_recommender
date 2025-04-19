# Use the official lightweight Python image
FROM python:3.10-slim

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

WORKDIR /app

COPY . /app
RUN pip install --upgrade pip && pip install -r requirements.txt

CMD ["python", "run.py"]
