FROM python:3.9

WORKDIR /app

COPY requirements.txt .

RUN pip install -r requirements.txt

COPY main.py .
COPY templates templates

EXPOSE 8085

CMD ["python", "main.py"]
