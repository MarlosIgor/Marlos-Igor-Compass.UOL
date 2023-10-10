import json
import boto3
import requests
from datetime import datetime

REGIAO_AWS = 'us-east-1'
ID_ACESSO_IAM_AWS = 'AKIAVMELNHFF7MWZ22ZS'
CHAVE_SECRETA_IAM_AWS = '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'
TMDB_API_KEY = 'cdfe43627e7ecf677ae84cd7fee138e2'

TIPOS_MIDIA = {'tv': 'Series',
               'movie': 'Movies'}

GENEROS = {'28,12': 'Ação-Aventura',
           '28': 'Ação',
           '12': 'Aventura',
           '10759': 'Ação-Aventura'}


def obter_dados_tmdb(pagina, tipo_midia, genero):
    url = (f"https://api.themoviedb.org/3/discover/{tipo_midia}?api_key={TMDB_API_KEY}&"
           f"language=pt-BR&sort_by=popularity.desc&include_adult=false&"
           f"include_video=false&page={pagina}&"
           f"with_genres={genero}")

    resposta = requests.get(url)
    return resposta.json()


def enviar_para_s3(dados, indice, tipo_midia, genero):
    s3 = boto3.client('s3', aws_access_key_id=ID_ACESSO_IAM_AWS,
                      aws_secret_access_key=CHAVE_SECRETA_IAM_AWS,
                      region_name=REGIAO_AWS)

    nome_bucket = 'data-lake-marlos-igor'
    nome_arquivo = (f'Raw/TMDB/JSON/{TIPOS_MIDIA[tipo_midia]}/{GENEROS[genero]}/'
                    f'{datetime.now().strftime("%Y/%m/%d")}/data_{indice}.json')
    s3.put_object(Body=json.dumps(dados), Bucket=nome_bucket, Key=nome_arquivo)


def processar_midia(tipo_midia, generos):
    for genero in generos:
        dados = obter_dados_tmdb(1, tipo_midia, genero)
        todos_resultados = dados.get('results', [])
        total_paginas = dados.get('total_pages', 1)

        for pagina in range(2, total_paginas + 1):
            dados = obter_dados_tmdb(pagina, tipo_midia, genero)
            todos_resultados.extend(dados.get('results', []))

        for i in range(0, len(todos_resultados), 100):
            pedaco = todos_resultados[i:i + 100]
            enviar_para_s3(pedaco, i // 100, tipo_midia, genero)


def lambda_handler(event, context):
    try:
        processar_midia('movie', ['28,12', '28', '12'])
        processar_midia('tv', ['10759'])

        return {
            'statusCode': 200,
            'body': json.dumps('Upload para o S3 realizado com sucesso!')
        }
    except Exception as e:
        return {
            'statusCode': 500,
            'body': json.dumps(f'Erro: {str(e)}')
        }

