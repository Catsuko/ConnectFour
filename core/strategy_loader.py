from os import listdir
from os.path import isfile, join, basename
import re
from importlib import import_module    

class StrategyLoader:
    
    def __init__(self, player_dir):
        self.players = []
        self.player_dir = player_dir

    def find_and_load(self):
        python_files = [file for file in listdir(self.player_dir) if isfile(join(self.player_dir, file)) and re.search("[a-zA-Z_0-9]+[\.][p][y]",file)]
        [self._import_from_file(file) for file in python_files if file != "__init__.py"]

    def _import_from_file(self, file_name):
        file = open(join(self.player_dir, file_name))
        content = file.read()        
        file.close()        
        package = re.sub("\.\/", "", self.player_dir)
        module_name = re.sub("\.py", "", file_name)
        new_module = import_module(package+"."+module_name,".")
        self.players.append(new_module.create_strategy())
    
    def __len__(self):
        return len(self.players)
    
    def __getitem__(self, key):
        return self.players[key]