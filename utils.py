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
    
    