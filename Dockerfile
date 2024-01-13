# docker build -t nineking424/pybitmex .
# docker image inspect nineking424/pybitmex
 FROM python:3.10-alpine

COPY app /app
WORKDIR /app

RUN python3 -m pip install -r requirements.txt

CMD ["python3", "wsdump_test.py"]