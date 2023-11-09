# Dockerfile para carguru.py
FROM python:3.9

WORKDIR /app

COPY carguru.py .

RUN pip install requests

CMD ["python", "carguru.py"]

# cria uma imagem: docker build -t carguru .
# executa um contêiner: docker run -d -it --name carguru --rm carguru
