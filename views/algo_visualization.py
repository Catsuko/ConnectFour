import time

class AlgoVisualization():

    def __init__(self, arr):
        self.arr = arr
        self.checks = []

    def __len__(self):
        return len(self.arr)
    
    def __getitem__(self, key):
        self.checks.append(key)
        return self.arr[key]

    def clear(self):
        self.checks = []

    def print_all(self):
        width = len(self)
        for i in self.checks:
            line = ['X' if x == i else ' ' for x in range(len(self))]
            print('[%s]' % ''.join(line), end='\r', flush=True)
            time.sleep(0.2)
        print()
                
