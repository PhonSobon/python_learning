## Exercise

# on the company have employess 100 and empoyees have salary more than 1000$ need to pay tax 5%
# and if the empoyess have salaray less than 1000$ need to pay tax 2% and employess less than 500$ no tax
# CEo want to know how much tax he need to pay for all employess
# CEO want to know that how many employess have sarlary more than 1000$

## Solution

# 1. Create a list of employees with their salaries

employees = [
    {"name": "John", "salary": 1200},
    {"name": "Jane", "salary": 800},
    {"name": "Doe", "salary": 400},
    {"name": "Alice", "salary": 1500},
    {"name": "Bob", "salary": 600},
]

# 2. Initialize variables to keep track of total tax and number of employees with salary > 1000
total_tax = 0
count_above_1000 = 0

# 3. Iterate through the list of employees
for employee in employees:
    salary = employee["salary"]
    
    # 4. Check the salary and calculate tax accordingly
    if salary > 1000:
        tax = salary * 0.05
        count_above_1000 += 1
    elif salary > 500:
        tax = salary * 0.02
    else:
        tax = 0
    
    # 5. Add the tax to the total tax
    total_tax += tax


# 6. Print the results
print(f"Total tax to be paid: ${total_tax:.2f}")
print(f"Number of employees with salary > 1000: {count_above_1000}")
# 7. The code is easy to read and understand, and it is a good example of how to use nested if-else statements in Python.
# 8. However, it could be improved by using a dictionary to store the tax rates and their corresponding ranges.
# 9. This would make the code more concise and easier to maintain.