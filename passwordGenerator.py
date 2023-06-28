import string
import random

def generate_password(password_length):

# Initiate all types of characters. Each value is string
    if int(password_length) >= 4:
        uppercase = string.ascii_uppercase
        lowercase = string.ascii_lowercase
        numbers = string.digits
        special = string.punctuation
        all_chars = uppercase + lowercase + numbers + special # concatenate all characters  
        pas = random.choice(uppercase) + random.choice(lowercase) + random.choice(numbers) + random.choice(special)
        char_generation_counter = int(password_length) - 4
        print("\n" + str(char_generation_counter) + " additional characters to be generated in order to complete the password\n")
        while char_generation_counter != 0:
            pas = pas + random.choice(all_chars)
            char_generation_counter -= 1

    else:
        pas = "Requested password lenght is less than 4 characters"

    return pas

password_length = input("Type desired password length (at least 4 symbols) and press enter\n")

password = generate_password(password_length)    
print("Please enjoy your strong and secure password! It is shown on a next line\n" + password)
print("\n ----------------------\nFor review: \nrequested length: " + password_length + "\nactual lenght: " + str(len(password)))