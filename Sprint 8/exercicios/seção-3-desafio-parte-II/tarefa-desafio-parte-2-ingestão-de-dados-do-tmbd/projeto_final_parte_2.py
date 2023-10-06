import json
import boto3
import requests
from datetime import datetime

AWS_REGION = 'us-east-1'

AWS_IAM_ACCESS_KEY_ID = 'AKIAVMELNHFFZ2XGFWPU'

AWS_IAM_SECRET_ACCESS_KEY = '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'

def get_movies_page(page, media_type, genre):
    url = f"https://api.themoviedb.org/3/discover/{media_type}?api_key=cdfe43627e7ecf677ae84cd7fee138e2&language=pt-BR&sort_by=popularity.desc&include_adult=false&include_video=false&page={page}&with_genres={genre}"
    response = requests.get(url)
    data = response.json()
    return data


def upload_to_s3(data, index, media_type):
    s3 = boto3.client('s3', aws_access_key_id=AWS_IAM_ACCESS_KEY_ID,
                      aws_secret_access_key=AWS_IAM_SECRET_ACCESS_KEY,
                      region_name=AWS_REGION)

    bucket_name = 'data-lake-marlos-igor'
    file_name = f'Raw/TMDB/JSON/{media_type}/{datetime.now().strftime("%Y/%m/%d")}/data_{index}.json'
    s3.put_object(Body=json.dumps(data), Bucket=bucket_name, Key=file_name)


def lambda_handler(event, context):
    try:
        genre = 'Ação/Aventura'

        movies_data = get_movies_page(1, 'movie', '28,12')
        series_data = get_movies_page(1, 'tv', '10759')

        total_movies_pages = movies_data['total_pages']
        total_series_pages = series_data['total_pages']

        all_movies_results = movies_data['results']
        all_series_results = series_data['results']

        for page in range(2, total_movies_pages + 1):
            movies_data = get_movies_page(page, 'movie', '28,12')
            all_movies_results.extend(movies_data['results'])

        for page in range(2, total_series_pages + 1):
            series_data = get_movies_page(page, 'tv', '10759')
            all_series_results.extend(series_data['results'])

        for i in range(0, len(all_movies_results), 100):
            chunk = all_movies_results[i:i + 100]
            upload_to_s3(chunk, i // 100, 'movie')

        for i in range(0, len(all_series_results), 100):
            chunk = all_series_results[i:i + 100]
            upload_to_s3(chunk, i // 100, 'tv')

        return {
            'statusCode': 200,
            'body': json.dumps('Upload para o S3 realizado com sucesso!')
        }
    except Exception as e:
        return {
            'statusCode': 500,
            'body': json.dumps(f'Erro: {str(e)}')
        }

