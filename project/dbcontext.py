class Dbcontext:
    def __init__(self):
        self.host = "data.db"
        self.connection = None
    def __enter__(self):
        self.connection = sqlite3.connect(self.host)
        
    