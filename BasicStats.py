#. Basic summary statistics example
#. Author: @dspk

grades = [100, 100, 90, 40, 80, 100, 85, 70, 90, 65, 90, 85, 50.5]

#. A function to print out the list of grades
def print_grades(grades):
    for grade in grades:
        print grade

#. A function to compute the sum of the test grades. 
def grades_sum(grades):
    total = 0
    for grade in grades: 
        total += grade
    return total

#. A function to compute the average of the grades and return the average grade
def grades_average(grades):
    sum_of_grades = grades_sum(grades)
    average = sum_of_grades / len(grades)
    return average

#. A function to compute the variance and return the computed variance
def grades_variance(grades, average):
    numerator = 0
    for grade in grades:
        numerator += (grade - average)**2
        grades_variance = numerator/len(grades)
    return grades_variance

average = grades_average(grades)
print grades_variance(grades, average)

#. A function to compute the standard deviation of the grades
import math
def grades_std_deviation(variance):
    grades_std_deviation = math.sqrt(variance)
    return grades_std_deviation

variance = grades_variance(grades, average)
print grades_std_deviation(variance)

#. Print out all the summary statistics
print_grades(grades)
print grades_sum(grades)
print grades_average(grades)
print grades_variance(grades, average)
print grades_std_deviation(variance)