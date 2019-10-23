from os import listdir
from os.path import isfile, join, basename
import re
from importlib import import_module
from core.errors import InsufficientStrategiesError

class StrategyLoader:
    
    def __init__(self, strategies_dir):
        self.strategies = []
        self.strategies_dir = strategies_dir

    def find_and_load(self):
        self.strategies.clear()
        python_files = [file for file in listdir(self.strategies_dir) if isfile(join(self.strategies_dir, file)) and re.search("[a-zA-Z_0-9]+[\.][p][y]",file)]
        [self._import_from_file(file) for file in python_files if file != "__init__.py"]
        if len(self) < 2:
            raise InsufficientStrategiesError("Less that two strategies were found.")

    def _import_from_file(self, file_name):
        file = open(join(self.strategies_dir, file_name))
        content = file.read()        
        file.close()        
        package = re.sub("\.\/", "", self.strategies_dir)
        module_name = re.sub("\.py", "", file_name)
        new_module = import_module(package+"."+module_name,".")
        self.strategies.append(new_module.create_strategy())
    
    def __len__(self):
        return len(self.strategies)
    
    def __getitem__(self, key):
        return self.strategies[key]