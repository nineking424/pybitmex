 FROM python:3.10-alpine

COPY app /app
WORKDIR /app

RUN python3 -m pip install -r requirements.txt

CMD ["python3", "pybitmex.py"]
