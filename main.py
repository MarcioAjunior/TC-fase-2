if __name__ == '__main__':
    from get_file import get_file
    from process_file import process_file
    
    if get_file():
        print('ARQUIVO BAIXADO E MOVIDO COM SUCESSO')
        if process_file():
            print('ARQUIVO PROCESSADO COM SUCESSO')
            if True:       
                print('ARQUIVO ENVIADO COM SUCESSO')
    