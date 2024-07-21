import os
import datetime
import re

def modification_date(file, path):
    complet_workdir = os.path.join(path, file)
    return os.path.getmtime(complet_workdir)

class Utils:
    @staticmethod
    def get_latest_file(path='', startswith='') -> str :
        files = [f for f in os.listdir(path) if f.startswith(startswith)]
      
        latest_file = max(files, key=lambda file: modification_date(file, path))

        return latest_file
    
    @staticmethod
    def clean_csv(line):
        replacements = {
            'á': 'a',
            'â': 'a',
            'à': 'a',
            'é': 'e',
            'ê': 'e',
            'í': 'i',
            'ó': 'o',
            'ô': 'o',
            'ú': 'u',
            'ü': 'u',
            'ç': 'c',
            'ñ': 'n',
            'ã': 'a',
            'õ': 'o',
            '@': 'A',
            '#': '',
            '%': 'percent',
            '$': '',
            '&': 'E',
            '*': 'x',
        }
        
        line = line.rstrip('\n')
        
        clened_line =  ''.join(replacements.get(c, c) for c in line)      
        
        return clened_line
    
    @staticmethod
    def get_date_from_str(str = ''): 
        try:
            
            str = re.search(r'[0-9]{2}-[0-9]{2}-[0-9]{4}', str).group()
            
            date = list(map(lambda x : int(x), str.split('-')))
            date = datetime.datetime(day=date[0], month=date[1], year=date[2])
            return date
        except Exception as e:
            print(e)
            return None
    
    @staticmethod 
    def multiple_replace(str = ''):
        
        matches = re.findall(r'[/\.\s+]' ,str)
        
        for match in matches:
            if match == '.':
                str = str.replace(match, '')
                continue
            str = str.replace(match, '-')
        
        return str
    