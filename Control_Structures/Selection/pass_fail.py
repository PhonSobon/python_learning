# Exercise 1.2.1 : write a program that ask the user for input of a grade student has received pass and fail
name = input("Enter student name: ")
grade = input("Enter student grade: ")
math = int(input("Enter math grade: "))
physics = int(input("Enter physics grade: "))
chemistry = int(input("Enter chemistry grade: "))

average = (math + physics + chemistry) / 3

if average <= 100 or average >= 90:
    print(f"{name} has passed with average grade of {average}")
elif average < 90 and average >= 80 :
    print(f"{name} has a grade of {average} and needs to work hard")
elif average < 80 and average >= 70:
    print(f"{name} has a grade of {average} and needs to work harder")
elif average < 70 and average >= 60:
    print(f"{name} has a grade of {average} and needs to work very hard")
elif average < 60 and average >= 50:
    print(f"{name} has a grade of {average} and needs to work extremely hard")
else:
    print(f"{name} has failed with an average grade of {average}. Please try again next time.")
