class Student:
    def __init__(self, first_name, last_name, slack_handle, cohort):
        self.first_name = first_name
        self.last_name = last_name
        self.slack_handle = slack_handle
        self.cohort = cohort
        self.exercises = list()
        
    def list_exercises(self):
        
        exercises = ", ".join(self.exercises)
        # print(exercises)
        print(f"{self.first_name} is working on {exercises}.")
        