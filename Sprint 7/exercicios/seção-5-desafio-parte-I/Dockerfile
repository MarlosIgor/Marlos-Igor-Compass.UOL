FROM python:3.8

RUN pip install boto3

ENV AWS_ACCESS_KEY_ID AKIAVMELNHFFZ2XGFWPU
ENV AWS_SECRET_ACCESS_KEY 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

WORKDIR /app

VOLUME /data

COPY desafio-parte-1-etl.py /app/desafio-parte-1-etl.py

CMD ["python", "desafio-parte-1-etl.py"]


# docker build -t desafio-final-parte1-etl .

# docker run -v /home/marlos-igor/projeto-final-01/parte-1:/data desafio-final-parte1-etl
