class Exercise:
    def __init__(self, name, language):
        self.name = name
        self.language = language
        
    def __str__(self):
        print(f"Exercise {self.name} for {self.language}")