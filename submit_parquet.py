import os
import boto3
from utils import Utils
import datetime

BUCKET = 'fiap-tc-fase2-ml'
WORKDIR = './/docs//03parquet'
BASE_FOLDER = 'RAW'


def submit_parquet():
    try:
        
        s3_client = boto3.client('s3')
        absolute_parquet = os.path.abspath(WORKDIR)
        
        today_str = datetime.datetime.today().strftime("%d-%m-%Y")

        latest_file = Utils.get_latest_file(absolute_parquet,'processed_parquet')

        target = '{}/raw_parquet_{}'.format(BASE_FOLDER, today_str)       

        s3_client.upload_file(os.path.join(WORKDIR, latest_file), BUCKET, target)
        
        return True
    
    except Exception as e:
        print('Erro ao enviar arquivo para AWS S3 ', e)
        return False
    