class Bucket:
    def __init__(self, fr):
        self.fr = fr  
        self.entries = []  
        self.overflow = None  

    def is_full(self):
        return len(self.entries) >= self.fr