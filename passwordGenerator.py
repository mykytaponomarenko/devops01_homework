import string
import random

def generatePassword(passwordLength):

# Initiate all types of characters. Each value is string
    if int(passwordLength) >= 4:
        uppercase = string.ascii_uppercase
        lowercase = string.ascii_lowercase
        numbers = string.digits
        special = string.punctuation
        allSymbols = uppercase + lowercase + numbers + special # concatenate all symbols  
        pas = random.choice(uppercase) + random.choice(lowercase) + random.choice(numbers) + random.choice(special)
        symbolsGenerationCount = int(passwordLength) - 4
        print(str(symbolsGenerationCount) + " characters to be generated in order to complete the password")
        while symbolsGenerationCount != 0:
            pas = pas + random.choice(allSymbols)
            symbolsGenerationCount -= 1

    else:
        pas = "Requested password lenght is less than 4 characters"

    return pas

passwordLength = input("Type desired password length (at least 4 symbols) and press enter\n")

password = generatePassword(passwordLength)    
print(password + ", requested length: " + passwordLength + ", actual lenght: " + str(len(password)))