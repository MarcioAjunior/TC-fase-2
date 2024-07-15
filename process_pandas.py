import pandas as pd
import os
from utils import Utils
import datetime

WORKDIR = ".//docs//02processed_csv"
SAVE_DIR = ".//docs//03parquet"

def process_pandas():
    try:
        latest_file = Utils.get_latest_file(WORKDIR, 'processed_csv')
        
        column_names = ["codigo", "acao", "tipo", "qtd_teorica", "part", "break_line"]
            
        absolute_processed_csv = os.path.abspath(WORKDIR)
        absolute_processed_parquet = os.path.abspath(SAVE_DIR)
        
        today_str = datetime.datetime.today().strftime("%d-%m-%Y")
        
        df = pd.read_csv(f'{absolute_processed_csv}//{latest_file}', sep=';', header=1, names=column_names, decimal=',')
        
        column_names.remove("break_line")
        df = df[column_names]
        
        df['tipo'] = df['tipo'].str.replace(r'\s+', '-', regex=True)
        df.to_parquet(f'{absolute_processed_parquet}\\processed_parquet_{today_str}.parquet', engine='pyarrow')
        
        return True
    except Exception as e :
        print('Não foi possivel processar e criar PARQUET ', e)
        return False
        
    