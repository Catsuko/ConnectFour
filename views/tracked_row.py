class TrackedRow():

    def __init__(self, arr, row_index):
        self.arr = arr
        self.access_indices = []
        self.row_index = row_index

    def __len__(self):
        return len(self.arr)

    def __getitem__(self, key):
        self.access_indices.append(key)
        return self.arr[key]

    def clear(self):
        self.access_indices = []

    def read_all(self):
        return [(x, self.row_index) for x in self.access_indices]
