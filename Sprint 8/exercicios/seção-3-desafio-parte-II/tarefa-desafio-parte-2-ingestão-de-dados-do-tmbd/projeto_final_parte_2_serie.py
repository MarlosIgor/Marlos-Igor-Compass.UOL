import pandas as pd
import requests
import boto3
from concurrent.futures import ThreadPoolExecutor
import json
from datetime import datetime
import logging

from requests import RequestException

logging.getLogger().setLevel(logging.INFO)

REGIAO_AWS = 'us-east-1'
ID_ACESSO_IAM_AWS = 'xxx'
CHAVE_SECRETA_IAM_AWS = 'xxx'
TMDB_API_KEY = 'xxx'


def consultar_api_tmdb(id_imdb: str):
    try:
        logging.info(f'Consultando a API do TMDB para o ID {id_imdb}')
        find_url = f'https://api.themoviedb.org/3/find/{id_imdb}?api_key={TMDB_API_KEY}&external_source=imdb_id'
        response = requests.get(find_url)
        find_data = json.loads(response.content)

        if find_data['tv_results']:
            id_serie = find_data['tv_results'][0]['id']

            url = f"https://api.themoviedb.org/3/tv/{id_serie}?api_key={TMDB_API_KEY}&append_to_response=credits"
            response = requests.get(url)
            serie = json.loads(response.content)

            return serie
    except RequestException as e:
        logging.error(f'Erro ao consultar a API do TMDB: {e}')
        return None


def lambda_handler(event, context):
    s3_client = boto3.client('s3', region_name=REGIAO_AWS, aws_access_key_id=ID_ACESSO_IAM_AWS,
                             aws_secret_access_key=CHAVE_SECRETA_IAM_AWS)

    s3_bucket = 'data-lake-marlos-igor'
    s3_csv_path = 'Raw/Local/CSV/Series/2023/10/12/series.csv'

    s3_csv_object = s3_client.get_object(Bucket=s3_bucket, Key=s3_csv_path)
    df = pd.read_csv(s3_csv_object['Body'], sep='|', low_memory=False)
    df = df.drop_duplicates(subset='id')
    df_filtrado = df[
        (df['genero'].isin(['Action', 'Adventure'] or ['Action'] or ['Adventure'])) & (df['genero'] != "[]")]

    with ThreadPoolExecutor() as executor:
        novos_dados = [data for data in executor.map(consultar_api_tmdb, df_filtrado['id']) if data is not None]

    grupos_dados = [novos_dados[i:i + 100] for i in range(0, len(novos_dados), 100)]

    for i, grupo in enumerate(grupos_dados):
        try:
            json_body = json.dumps(grupo)
            if len(json_body) < 10 * 1024 * 1024:
                s3_key=f'Raw/TMDB/JSON/Series/{datetime.now().strftime("%Y/%m/%d")}/series_{i}.json'
                logging.info(f'Enviando dados para o S3: {s3_bucket}/{s3_key}')
                s3_client.put_object(
                    Body=json_body,
                    Bucket=s3_bucket,
                    Key=s3_key
                )
        except Exception as e:
            logging.error(e)

    return {
        'statusCode': 200,
        'body': 'Dados capturados com sucesso!'
    }

