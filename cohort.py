class Cohort:
    def __init__(self, name):
        self.name = name
        self.students = list()
        self.instructors = list()
    
    def __str__(self):
        print(f"{self.name}")