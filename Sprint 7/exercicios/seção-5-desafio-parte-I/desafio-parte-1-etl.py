import os
import boto3
from datetime import datetime

aws_access_key_id = os.environ['AWS_ACCESS_KEY_ID']
aws_secret_access_key = os.environ['AWS_SECRET_ACCESS_KEY']

s3 = boto3.client('s3',
                  aws_access_key_id=aws_access_key_id,
                  aws_secret_access_key=aws_secret_access_key)

source_directory = "/data"
s3_bucket = "data-lake-marlos-igor"
s3_prefix = "Raw/Local/CSV"

files_to_upload = ["movies.csv", "series.csv"]

for file_name in files_to_upload:

    folder_name = os.path.splitext(file_name)[0].capitalize()
    s3_key = f"{s3_prefix}/{folder_name}/{datetime.now().strftime('%Y/%m/%d')}/{file_name}"

    s3.upload_file(os.path.join(source_directory,
                   file_name), s3_bucket, s3_key)
    print(f"Arquivo {file_name} carregado com sucesso para o S3.")

