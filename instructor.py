class Instructor:
    def __init__(self, first_name, last_name, slack_handle, cohort, specialty):
        self.first_name = first_name
        self.last_name = last_name
        self.slack_handle = slack_handle
        self.cohort = cohort
        self.specialty = specialty
    
    def __str__(self):
        print(f"Instructor | First Name: {self.first_name}, Last Name: {self.last_name}, Slack Handle: {self.slack_handle}, Cohort: {self.cohort}, Specialty: {self.specialty}")
        
    # A method to assign an exercise to a student
    def assign_exercise(self, student, exercise):
        student.exercises.append(exercise)
        