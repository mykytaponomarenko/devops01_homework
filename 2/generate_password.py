#!/usr/env python

from settings import change_settings
import string
import random

uppercase = string.ascii_uppercase
lowercase = string.ascii_lowercase
digits = string.digits
specials = string.punctuation

class PasswordGenerator:
 def __init__(self, settings=None):
  
  if settings is None:                           
   settings = {                           # assigning default settings
               'length': 8, 
               'include_uppercase' : True,
               'include_lowercase' : True,
               'include_digits' : True,
               'include_special_chars' : True,
               }
  self.settings = settings

 def generate_password(self):

  # Collect symbols for password generation 
  chars = [
   uppercase if self.settings['include_uppercase'] else '',
   lowercase if self.settings['include_lowercase'] else '',
   digits if self.settings['include_digits'] else '',
   specials if self.settings['include_special_chars'] else '',
  ]
  chars = ''.join(chars)    # password will be generator from those 
  
  # Generate 1 symbol per each enabled type
  password  = [
   random.choice(uppercase) if self.settings['include_uppercase'] else '',
   random.choice(lowercase) if self.settings['include_lowercase'] else '',
   random.choice(digits) if self.settings['include_digits'] else '',
   random.choice(specials) if self.settings['include_special_chars'] else '',
  ]
  password = ''.join(password)

  while len(password) < self.settings['length']:
   password += random.choice(chars)

  print('Your password is displayed on the next line\n' + password)
  

 def show_settings(self):
  print("Settings: " + str(self.settings))
 
 def change_settings(self):
    change_settings(self.settings)

print('\nWelcome to Password Generator!')
