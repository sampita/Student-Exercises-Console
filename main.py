from student import Student
from instructor import Instructor
from cohort import Cohort
from exercise import Exercise

# Create 4, or more, exercises.
exercise_one = Exercise("Urban Planner", "Python")
exercise_two = Exercise("Chicken Monkey", "JavaScript")
exercise_three = Exercise("Daily Journal", "JavaScript")
exercise_four = Exercise("Celebrity Tribute", "HTML")
exercise_five = Exercise("Pizza Joint", "Python")
# print(exercise_five)

# Create 3, or more, cohorts.
C36 = Cohort("Day Cohort 36")
E11 = Cohort("Evening Cohort 11")
C34 = Cohort("Day Cohort 34")
# print(C34)

# Create 4, or more, students and assign them to one of the cohorts.
student_one = Student("Sam", "Pita", "sampita", "C36")
student_two = Student("Melody", "Stern", "melodystern", "C36")
student_three = Student("Sarah", "Fleming", "sarahfleming", "C34")
student_four = Student("John", "Snow", "winteriscoming", "E11")
# print(student_four)

# Challenge: Create a list of students. Add all of the student instances to it.
studentsArray = [student_one, student_two, student_three, student_four]

# Create 3, or more, instructors and assign them to one of the cohorts.
instructor_one = Instructor("Jisie", "David", "jisiedavid", "C36", "Master of Explaining Things")
instructor_two = Instructor("Joe", "Shepherd", "joeshep", "C34", "Funny Man")
instructor_three = Instructor("Jenna", "Solis", "jsolis", "E11", "Elegant and Sweet")
# print(instructor_one)


# Have each instructor assign 2 exercises to each of the students.
instructor_one.assign_exercise(student_one, exercise_five.name)
instructor_one.assign_exercise(student_two, exercise_five.name)
instructor_two.assign_exercise(student_one, exercise_two.name)
instructor_two.assign_exercise(student_four, exercise_one.name)
instructor_three.assign_exercise(student_four, exercise_three.name)
instructor_three.assign_exercise(student_one, exercise_four.name)

# for exercise in student_one.exercises:
#     print(exercise.name)

# print(student_one.list_exercises)

for student in studentsArray:
    student.list_exercises()