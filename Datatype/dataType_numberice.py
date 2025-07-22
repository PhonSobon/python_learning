a = 20
b = 20.5
c = 20 + 5j
print(type(a))
print(type(b))
print(type(c))


# Output:
# <class 'int'>
# <class 'float'>
# <class 'complex'>

# Numeric data types in Python
# 1. int: Represents integer values.
# 2. float: Represents floating-point numbers (decimal values).
# 3. complex: Represents complex numbers, which have a real and an imaginary part.
# Numeric data types can be used in mathematical operations, and Python provides a wide range of built-in functions to work with them.

z1 = 3 + 4j
z2 = 1 - 2j

result = z1 + z2
print("Sum:", result)

# convert from int to float
a = 10
b = float(a)
print("Converted to float:", b)
# convert from float to int
a = 10.5
b = int(a)
print("Converted to int:", b)

# convert from int to complex
a = 10
b = complex(a)
print("Converted to complex:", b)
# convert from float to complex
a = 10.5
b = complex(a)
print("Converted to complex from float:", b)

# convert from complex to float (only the real part is taken)
a = 10 + 5j
b = float(a.real)
print("Converted to float from complex (real part):", b)


