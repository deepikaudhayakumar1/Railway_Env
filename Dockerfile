FROM python:3.9

WORKDIR /app

COPY . .

RUN pip install fastapi uvicorn requests openai pyyaml

CMD ["python", "inference.py"]