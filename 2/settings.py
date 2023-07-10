#!/usr/bin/env python

def change_settings(settings):   
  if settings['include_uppercase'] == 1:
   switch_upper = 'disable include_uppercase case'
  else:
    switch_upper = 'enable upper case'
  if settings['include_lowercase'] == 1:
   switch_lower = 'disable lower case'
  else:
    switch_lower = 'enable lower case'
  if settings['include_digits'] == 1:
    switch_number = 'disable numbers'
  else:
    switch_number = 'enable numbers'
  if settings['include_special_chars'] == 1:
    switch_special = 'disable special characters'
  else:
    switch_special = 'enable special characters'
  
  user = input('''
        Actions:
        1 - set password length
        2 - ''' + switch_upper + '''
        3 - ''' + switch_lower + '''
        4 - ''' + switch_number + '''
        5 - ''' + switch_special + '''
        0 - back
        ''')

  if user == '1':
    new_length = input('type new length value\n')
    settings['length'] = int(new_length)
  elif user == '2':
    settings['include_uppercase'] = not settings['include_uppercase']
  elif user == '3':
    settings['include_lowercase'] = not settings['include_lowercase']
  elif user == '4':
    settings['include_digits'] = not settings['include_digits']
  elif user == '5':
    settings['include_special_chars'] = not settings['include_special_chars']
  elif user == '0':
    pass
  else:
    print("Invalid command, back to main menu")
  