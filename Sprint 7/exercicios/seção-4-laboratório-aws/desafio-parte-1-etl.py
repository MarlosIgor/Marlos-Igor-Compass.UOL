import boto3
import os
from datetime import datetime

os.environ['AWS_ACCESS_KEY_ID'] = 'AKIAVMELNHFFVNEVPOEJ'
os.environ['AWS_SECRET_ACCESS_KEY'] = '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'


source_directory = "/data"
s3_bucket = "marlos-igor"
s3_prefix = "Raw/Local/CSV"

s3 = boto3.client("s3")

files_to_upload = ["movies.csv", "series.csv"]

for file_name in files_to_upload:

    folder_name = os.path.splitext(file_name)[0].capitalize()
    s3_key = f"{s3_prefix}/{folder_name}/{datetime.now().strftime('%Y/%m/%d')}/{file_name}"

    s3.upload_file(os.path.join(source_directory,
                   file_name), s3_bucket, s3_key)
    print(f"Arquivo {file_name} carregado com sucesso para o S3.")



