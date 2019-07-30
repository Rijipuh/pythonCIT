# test code
# # name = input()
# # print("hi ! I am " + name)
#
# name = input("What is your name? ")
# print ("my name is " + name)
# age = input("What is your age? ")
# # # print(type(age))
# print("Next year, I am "+ str(int(age) + 1))
# print("Next year, I am {}".format(int(age) + 1) )
# print ( int(age) + 1)
# # print ( type(int(age) + 1))

# name
# age
# gender
# race
# height
# weight
# grade
#
# ===== NAME's Profile ======
# Name : NAME     Gender : M/F
# age : Age       Race : black
# height :
# weight :
# BMI :  // weight(kg) / height(m)^2
# grade :
# graduation year :
# =============================




reportForm = """
===== {}'s Profile =====
Name  :  {}  Gender :  {}
age : {}     Race  : {}
height : {}
weight : {}
Bmi : {}
Grade: {}
Graduation Year: {}
=========================
"""

Name = input("What is your name? ")
Age = input("What is your age? ")
Gender = input("Are you male or female ")
Race = input("What race are you? ")
Height = input("What is your height in meters ")
Weight = input("What is your weight in kg ")
Grade = input("What grade are you in? ")

GraduationYear = (12-int(Grade) + 2020)
BMI = round((int(Weight)/(float(Height)**2)), 3)

print (reportForm.format(Name, Name, Gender, Age, Race, Height, Weight, BMI, Grade, GraduationYear  ))
