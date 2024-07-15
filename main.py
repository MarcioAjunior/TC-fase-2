if __name__ == '__main__':
    from get_file import get_file
    from process_file import process_file
    from process_pandas import process_pandas
    from submit_parquet import submit_parquet
    
    if get_file() : #get_file()
        print('ARQUIVO BAIXADO E MOVIDO COM SUCESSO')
        if process_file():
            print('ARQUIVO PROCESSADO COM SUCESSO')
            if process_pandas():
                print('DATAFRAME PROCESSADO COM SUCESSO')
                if submit_parquet():       
                    print('ARQUIVO ENVIADO PARA AWS COM SUCESSO')
    