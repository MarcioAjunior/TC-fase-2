from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import os
import shutil
import os
from utils import Utils

DOWNLOAD_DIR = "C:\\Users\\marci\\Downloads"
WORKDIR = ".//docs//csv"

def get_file():
    try:
        driver = webdriver.Chrome()
        driver.get("https://sistemaswebb3-listados.b3.com.br/indexPage/day/IBOV?language=pt-br")

        wait = WebDriverWait(driver, 10)
        btn_download = wait.until(EC.element_to_be_clickable((By.XPATH, '//a[@href="/indexPage/day/IBOV?language=pt-br"]')))

        btn_download.click()
        
        time.sleep(2)
    except Exception as e :
        print('Erro ao capturar arquivo' , e)
        return False
    finally:
        driver.quit()
        
    try:
        latest_file = Utils.get_latest_file(DOWNLOAD_DIR, 'IBOVDia')
        
        file_move = os.path.join(DOWNLOAD_DIR, latest_file)
        
        shutil.move(file_move, WORKDIR)
        
    except shutil.Error as e:
        if "already exists" in str(e):
            print(f"O arquivo já existe no destino...")
            return True
        print('Erro ao mover o arquivo ',e)
        return False
    except Exception as e:
        print('Erro ao mover o arquivo ',e)
        return False
    
    return True
