#. Student grades example 
#. Author: @dspk

#. Create three dictionaries: dave, nicole, and steve. Give each dictionary the keys "name", "homework", "quizzes", and "tests".
dave = {
    "name": "Dave",
    "homework": [90.0, 97.0, 75.0, 92.0],
    "quizzes": [88.0, 40.0, 94.0],
    "tests": [75.0, 90.0]
}
nicole = {
    "name": "Nicole",
    "homework": [100.0, 92.0, 98.0, 100.0],
    "quizzes": [82.0, 83.0, 91.0],
    "tests": [89.0, 97.0]
}
steve = {
    "name": "Steve",
    "homework": [0.0, 87.0, 75.0, 22.0],
    "quizzes": [0.0, 75.0, 78.0],
    "tests": [100.0, 100.0]
}

#. Put the dictionaries in a list called students
students = [dave, nicole, steve]

#Print out all the data in students list
for student in students:
    print student['name']
    print student['homework']
    print student['quizzes']
    print student['tests']

#. A function that calculates average of a list. 
def average(grades):
    avg = sum(grades[0:])/len(grades)
    return avg

#. A function that takes a (student) dictionary as input and returns his/her weighted average.
def get_average(student):
    wtd = 0.10*average(student['homework']) + 0.30*average(student['quizzes']) + 0.60*average(student['tests'])
    return wtd

#. A function that takes score as input and returns a string with the letter grade that that student should receive.
def get_letter_grade(score):
    if score >= 90:
        return "A"
    elif score >= 80 and score < 90:
        return "B"
    elif score >= 70 and score < 80:
        return "C"
    elif score >= 60 and score < 70:
        return "D"
    else:
        return "F"

#. A function that takes the class list as an argument to compute the average of the entire class.
#define class averages
def get_class_average(students):
    avgsum = 0
    for student in students:
        avgsum += get_average(student)
        classavg = avgsum/len(students)
    return classavg

#. Print the average for the class.  
print get_class_average(students)
#. Print the letter grade for any student.  
print get_letter_grade(get_average(nicole))
