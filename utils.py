import os

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
    