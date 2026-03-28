# ==============================
# BASIC PYTHON PRACTICE
# ==============================

# Input / Output
name = input("What is your name? ")
print("Hello " + name)

# Multiple input
x, y = input("Enter two numbers: ").split()
print(x, y)

# Type casting
int_x = int(input("Enter integer X: "))
float_y = float(input("Enter float Y: "))
print("Integer X:", int_x)
print("Float Y:", float_y)

# String formatting
name = "Shilpashree"
age = 27
print("My name is {} and I am {} years old.".format(name, age))


# ==============================
# VARIABLES
# ==============================

x, y, z = 1, 2, 3
print(x, y, z)

# Swapping variables
a = 10
b = 20
a, b = b, a
print("Swapped values:", a, b)


# ==============================
# FUNCTION - COUNT CHARACTERS
# ==============================

def count_characters(word):
    count = 0
    for char in word:
        count += 1
    return count

word = input("Enter a word: ")
print("Character count:", count_characters(word))


# ==============================
# OPERATORS & CONDITIONS
# ==============================

a = 10
b = 5

print("Addition:", a + b)
print("Subtraction:", a - b)
print("Multiplication:", a * b)
print("Division:", a / b)
print("Floor Division:", a // b)
print("Modulus:", a % b)
print("Exponentiation:", a ** b)

if a > b:
    print("a is greater than b")
elif a < b:
    print("a is less than b")
else:
    print("a is equal to b")