## Nested if-else statements
# This program checks if a number is positive, negative, or zero
# and also checks if the positive number is even or odd.
# It uses nested if-else statements to achieve this.
#
# Get user input
number = int(input("Enter a number: "))


# Check if the number is positive, negative, or zero
if number > 0:
    print("The number is positive.")
    # Nested if-else to check if the positive number is even or odd
    if number % 2 == 0:
        print("The number is even.")
    else:
        print("The number is odd.")
elif number < 0:
    print("The number is negative.")
else:
    print("The number is zero.")

