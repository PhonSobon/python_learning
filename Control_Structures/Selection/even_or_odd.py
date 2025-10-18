# Excercise 1.2 : write a program that asks the user for a number and then prints whether the number is even or odd.

numbers = int(input("Enter a number: "))
if numbers % 2 == 0 :
    print(f"{numbers} is an even number.")
else:
    print(f"{numbers} is an odd number.")


