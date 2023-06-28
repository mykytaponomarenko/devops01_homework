print("Welcome to PyCalculator!") #welcome message

firstNumber = input("Type first integer and press enter\n")
print("-------------------\nWell done, you typed '" + firstNumber + "'\n-------------------")

secondNumber = input("Type second integer and press enter\n")
print("-------------------\nWell done, you typed '" + secondNumber + "'\n-------------------")

operationType = input("In order to select operation type related number:\n1. Addition\n2. Subtraction\n3. Multiplication\n4. Division\n")

if operationType == "1":
    print("-------------------\nAddition it is! Result is " + str(int(firstNumber) + int(secondNumber)) + "\n-------------------")

elif operationType == "2":
    print("-------------------\nSubstraction it is! Result is " + str(int(firstNumber) - int(secondNumber)) + "\n-------------------")

elif operationType == "3":
    print("-------------------\nMultiplication it is! Result is " + str(int(firstNumber) * int(secondNumber)) + "\n-------------------")

elif operationType == "4":
    if secondNumber == "0":
        print("-------------------\nYou can't divide by 0, don't be a fool :)\n-------------------")
    else: 
        print("-------------------\nDivision it is! Result is " + str(int(firstNumber) / int(secondNumber)) + "\n-------------------")
  
else: 
    print("-------------------\nInvalid option\n-------------------")