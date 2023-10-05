import json
import boto3
import requests
from datetime import datetime

TMDB_API_KEY = 'xxx'

GENRE_ID = '28,12'

AWS_REGION = 'us-east-1'

AWS_IAM_ACCESS_KEY_ID = 'xxx'

AWS_IAM_SECRET_ACCESS_KEY = 'xxx'

BUCKET_NAME = 'data-lake-marlos-igor'


def get_movies_page(page):
    url = f'https://api.themoviedb.org/3/discover/movie'
    params = {
        'api_key': TMDB_API_KEY,
        'language': 'pt-BR',
        'sort_by': 'popularity.desc',
        'with_genres': GENRE_ID,
        'page': page
    }
    response = requests.get(url, params=params)
    return response.json()


def upload_to_s3(data, index):
    s3 = boto3.client('s3',
                      aws_access_key_id=AWS_IAM_ACCESS_KEY_ID,
                      aws_secret_access_key=AWS_IAM_SECRET_ACCESS_KEY,
                      region_name=AWS_REGION)

    FILE_PATH = f'Raw/TMDB/JSON/{datetime.now().strftime("%Y/%m/%d")}/data_{index}.json'
    file_data = json.dumps(data).encode('utf-8')
    s3.put_object(Bucket=BUCKET_NAME, Key=FILE_PATH, Body=file_data)


def lambda_handler(event, context):
    try:
        data = get_movies_page(1)
        total_pages = data['total_pages']

        all_results = data['results']

        for page in range(2, total_pages + 1):
            data = get_movies_page(page)
            all_results.extend(data['results'])

        for i in range(0, len(all_results), 100):
            chunk = all_results[i:i + 100]
            upload_to_s3(chunk, i // 100)

        return {
            'statusCode': 200,
            'body': json.dumps('Upload para o S3 realizado com sucesso!')
        }
    except Exception as e:
        return {
            'statusCode': 500,
            'body': json.dumps(f'Erro: {str(e)}')
        }
