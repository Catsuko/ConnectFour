from os import listdir
from os.path import isfile, join, basename
import re
from importlib import import_module
from core.errors import InsufficientStrategiesError, MissingExportFunctionError

class StrategyLoader:
    
    def __init__(self, strategies_dir):
        self.strategies = []
        self.strategies_dir = strategies_dir

    def _find_and_load(self):
        self.strategies.clear()
        python_files = [file for file in listdir(self.strategies_dir) if isfile(join(self.strategies_dir, file)) and re.search("[a-zA-Z_0-9]+[\.][p][y]",file)]        
        [self._import_from_file(file) for file in python_files if file != "__init__.py"]
        if len(self) < 2:
            raise InsufficientStrategiesError("Less that two strategies were found.")

    def _import_from_file(self, file_name):
        package = re.sub("\.\/", "", self.strategies_dir)
        module_name = re.sub("\.py", "", file_name)
        new_module = import_module(package+"."+module_name,".")
        if "export_strategy" in dir(new_module):
            self.strategies.append(new_module.export_strategy())
        else:
            raise MissingExportFunctionError("Module in {file_name} is missing export_strategy.".format(**locals()))
    
    def get_all_players(self):
        self._find_and_load()
        return self.strategies
    
    def __len__(self):
        return len(self.strategies)
    
    def __getitem__(self, key):
        return self.strategies[key]