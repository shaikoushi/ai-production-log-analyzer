FROM python:3.11-slim

WORKDIR /app

COPY analyzer.py .
COPY logs/ logs/

RUN mkdir -p reports

CMD ["python", "analyzer.py"]
