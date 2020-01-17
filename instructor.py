class Instructor:
    def __init__(self, first_name, last_name, slack_handle, cohort, specialty):
        self.first_name = first_name
        self.last_name = last_name
        self.slack_handle = slack_handle
        self.cohort = cohort
        self.specialty = specialty
    
    # A method to assign an exercise to a student
    def assign_exercise(self, student, exercise):
        student.exercises.append(exercise)
        