from .tracked_row import TrackedRow

class TrackedGrid():

    def __init__(self, rows):
        self.rows = rows
        self.row_accesses = []

    def __len__(self):
        return len(self.rows)

    def __getitem__(self, key):
        tracked_row = TrackedRow(self.rows[key], key)
        self.row_accesses.append(tracked_row)
        return tracked_row

    def read_all(self):
        return [pos for row in self.row_accesses for pos in row.read_all()]
        
    
        
