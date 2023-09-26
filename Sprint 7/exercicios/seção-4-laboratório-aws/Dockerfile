FROM python:3.7

RUN pip install boto3

WORKDIR /app

VOLUME /data

COPY desafio-parte-1-etl.py /app/desafio-parte-1-etl.py

CMD ["python", "desafio-parte-1-etl.py"]

# docker build -t desafio-parte-1-etl .
# docker run -v /home/marlos-igor/sprint7/atv3:/data desafio-parte-1-etl