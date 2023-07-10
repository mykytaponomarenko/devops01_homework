#!/usr/env python

from settings import change_settings

class PasswordGenerator:
 def __init__(self, settings=None):
  
  if settings is None:                           
   settings = {                                          # assigning default settings
               'length': 8, 
               'include_uppercase' : True,
               'include_lower' : True,
               'include_digits' : True,
               'include_special_chars' : True
               }
  self.settings = settings

 def generate_password(self):
  # Add code to generate a password based on the settings
  print("Generating password...")

 def show_settings(self):
  print("Settings: " + str(self.settings))
 
 def change_settings(self):
    change_settings(self.settings)

print('\nWelcome to Password Generator!')
