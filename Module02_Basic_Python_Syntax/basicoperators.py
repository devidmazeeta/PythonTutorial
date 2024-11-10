# Arithmetic Operators (+, -, *, /, %, **, //)
from numpy.random.mtrand import operator

num1 = 2
num2 = 4
print(num1 * num2) # 8
print(num1 ** num2) # 16

# Comparison Operators (==, !=, >, <, >=, <=)
num3 = 10
num4 = 20

if num3 < num4:
    print("Condition satisfied")

# Logical Operators (and, or, not)
flag1 = True
flag2 = True
flag3 = False
flag4 = False

if flag1 and flag2:
    print("And passed")

if flag1 or flag3:
    print("Or passed")

if flag3 or flag4:
    print("Or passed")
else:
    print("Or failed")

if not flag3: # True
    print("Not passed")

# Assignment Operators (+=, -=, *=, /=)
number = 10
number += 20 # number = number + 20