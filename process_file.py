import os
from utils import Utils
import datetime
import csv

WORKDIR = ".//docs//01csv"
SAVE_DIR = ".//docs//02processed_csv"

def process_file():
    
    try :
        latest_file = Utils.get_latest_file(WORKDIR,'IBOVDia')
        
        with open(f'{WORKDIR}//{latest_file}', 'r') as file:
            content = file.readlines()
        
        clean_content = [Utils.clean_csv(line) for line in content]
        clean_content = [line.split(';') for line in clean_content]
        
        #Removendo footer 
        clean_content = clean_content[:-2]        
        
        today_str = datetime.datetime.today().strftime("%d-%m-%Y")
        
        absolute_processed_csv = os.path.abspath(SAVE_DIR)
                
        with open(f'{absolute_processed_csv}//processed_csv_{today_str}.csv', 'w+', newline='', encoding='utf-8') as file:
            writer = csv.writer(file, delimiter=';')
            writer.writerows(clean_content)
            
        return True
    
    except Exception as e:
        print('Erro ao processar o arquivo CSV', e)
        return False
        
    
   
    
    
    