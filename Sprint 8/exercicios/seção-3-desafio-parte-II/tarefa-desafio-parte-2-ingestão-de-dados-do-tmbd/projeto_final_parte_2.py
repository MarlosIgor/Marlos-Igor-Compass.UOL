import os
import pandas as pd
import requests
import boto3

from datetime import datetime
from concurrent.futures import ThreadPoolExecutor

REGIAO_AWS = os.environ['REGIAO_AWS']
ID_ACESSO_IAM_AWS = os.environ['ID_ACESSO_IAM_AWS']
CHAVE_SECRETA_IAM_AWS = os.environ['CHAVE_SECRETA_IAM_AWS']
TMDB_API_KEY = os.environ['TMDB_API_KEY']


def consultar_api_tmdb(args):
    id_imdb, tipo = args
    tipo = 'movie' if tipo == 'movies' else 'find' if tipo == 'series' else tipo
    """Função para consultar a API do TMDB"""
    url = f"https://api.themoviedb.org/3/{tipo}/{id_imdb}?api_key={TMDB_API_KEY}&external_source=imdb_id"
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()
    else:
        return None


def carregar_filtrar_dados(s3_client, s3_bucket, s3_csv_path):
    try:
        s3_csv_object = s3_client.get_object(Bucket=s3_bucket, Key=s3_csv_path)
        df = pd.read_csv(s3_csv_object['Body'], sep='|', low_memory=False, keep_default_na=False)
        df_filtrado = df[df['genero'].isin(['Action', 'Adventure'])]
        return df_filtrado
    except Exception as e:
        print(f"Erro ao carregar e filtrar dados: {e}")
        return None


def consultar_api_para_ids(df_filtrado, tipo):
    with ThreadPoolExecutor() as executor:
        novos_dados = list(executor.map(consultar_api_tmdb, [(id_imdb, tipo) for id_imdb in df_filtrado['id']]))
    return novos_dados


def persistir_dados_s3(s3_client, s3_bucket, novos_dados, caminho_s3):
    lotes_dados = [novos_dados[i:i + 100] for i in range(0, len(novos_dados), 100)]
    for i, lote in enumerate(lotes_dados):
        s3_client.put_object(
            Body=pd.Series(lote).to_json(orient='records'),
            Bucket=s3_bucket,
            Key=f'{caminho_s3}_{i}.json'
        )


def processar_dados(tipo, s3_client, s3_bucket):
    df_filtrado = carregar_filtrar_dados(s3_client, s3_bucket, f'Raw/Local/CSV/{tipo}/2023/10/12/{tipo.lower()}.csv')
    novos_dados = consultar_api_para_ids(df_filtrado, tipo.lower())
    persistir_dados_s3(s3_client, s3_bucket, novos_dados,
                       f'Raw/TMDB/JSON/{tipo}/{datetime.now().strftime("%Y/%m/%d")}/{tipo.lower()}')


def lambda_handler(event, context):
    s3_client = boto3.client('s3', region_name=REGIAO_AWS, aws_access_key_id=ID_ACESSO_IAM_AWS,
                             aws_secret_access_key=CHAVE_SECRETA_IAM_AWS)
    s3_bucket = 'data-lake-marlos-igor'
    processar_dados('Movies', s3_client, s3_bucket)
    processar_dados('Series', s3_client, s3_bucket)
    return {
        'statusCode': 200,
        'body': 'Dados capturados com sucesso!'
    }

