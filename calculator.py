# Addition function
def addition (a, b):
    result = int(a) + int(b)
    return str(result)

# substraction function
def substraction (a,b):
    result = int(a) - int(b)
    return str(result)

# multiplication function
def multiplication (a,b):
    result = int(a) * int(b)
    return str(result)

# division function
def division (a,b):
    if b == "0":
        result = "You can't divide by 0, don't be a fool :)"
    else: 
        result = int(a) / int(b)
    return str(result)


print("Welcome to PyCalculator!") #welcome message

# Collect values from user  
firstNumber = input("Type first integer and press enter\n")
print("-------------------\nWell done, you typed '" + firstNumber + "'\n-------------------")

secondNumber = input("Type second integer and press enter\n")
print("-------------------\nWell done, you typed '" + secondNumber + "'\n-------------------")

# User selects operation type

operationType = input("In order to select operation type related number:\n1. Addition\n2. Subtraction\n3. Multiplication\n4. Division\n")

if operationType == "1":
# Activate Addition flow
    result = addition(firstNumber, secondNumber)
    print("-------------------\nAddition it is! Result is '" + result + "'\n-------------------")

elif operationType == "2":
# Activate Substraction flow
    result = substraction(firstNumber, secondNumber)
    print("-------------------\nSubstraction it is! Result is '" + result + "'\n-------------------")

elif operationType == "3":
# Activate Multiplication flow
    result = multiplication(firstNumber, secondNumber)
    print("-------------------\nMultiplication it is! Result is '" + result + "'\n-------------------")

elif operationType == "4":
# Activate Division flow
    result = division(firstNumber, secondNumber)
    print("-------------------\nDivision it is! Result is '" + result + "'\n-------------------")

else: 
    print("-------------------\nInvalid option\n-------------------")