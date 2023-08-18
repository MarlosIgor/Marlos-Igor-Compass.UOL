# Dockerfile para hash_string.py
FROM python:3.9

WORKDIR /app

COPY hash_string.py .

RUN pip install requests

CMD ["python", "hash_string.py"]
# cria uma imagem: docker build -t mascarar-dados .
# executa um contêiner: docker run -d -it --name hash_string --rm mascarar-dados
