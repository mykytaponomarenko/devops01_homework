import string
import random

print("\nWelcome to PPG - PyPasswordGenerator!")

def generate_password(password_length):

# Initiate all types of characters. Each value is string
    if int(password_length) >= 4:
        uppercase = string.ascii_uppercase
        lowercase = string.ascii_lowercase
        numbers = string.digits
        special = string.punctuation
        all_chars = uppercase + lowercase + numbers + special # concatenate all characters

        # add required chars  
        pas = random.choice(uppercase) + random.choice(lowercase) + random.choice(numbers) + random.choice(special)

        # add chars needed to generate requested password length
        char_generation_counter = int(password_length) - 4
        print("\n" + str(char_generation_counter) + " additional characters to be generated in order to complete the password\n")
        while char_generation_counter != 0:
            pas = pas + random.choice(all_chars)
            char_generation_counter -= 1

        # fully randomize password char order    
        pas_as_list = [*pas]
        pas_randomized = random.sample(pas_as_list, len(pas_as_list))
        
        print("----------\nbefore random.sample vs after:")
        print(pas_as_list)
        print(pas_randomized)

        pas = ""
        for i in pas_randomized:
            pas = pas + i

    else:
        pas = "Requested password lenght is less than 4 characters"

    return pas

password_length = input("Type desired password length (at least 4 symbols) and press enter\n")

password = generate_password(password_length)  
print("\n----------\nFor review: \nrequested length: " + password_length + "\nactual lenght: " + str(len(password)) + "\n----------")  
print("Please enjoy your strong and secure password! It is shown on a next line\n" + password)
