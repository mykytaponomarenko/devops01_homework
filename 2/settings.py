#!/usr/bin/env python

def change_settings(settings):   
  if settings['UPPER'] == 1:
   upper_status = 'disable upper case'
  else:
    upper_status = 'enable upper case'
  if settings['lower'] == 1:
   lower_status = 'disable lower case'
  else:
    lower_status = 'enable lower case'
  if settings['numb6r'] == 1:
    number_status = 'disable numbers'
  else:
    number_status = 'enable numbers'
  if settings['speci@l'] == 1:
    special_status = 'disable special characters'
  else:
    special_status = 'enable special characters'
  
  user = input('''
        Actions:
        1 - set password length
        2 - ''' + upper_status + '''
        3` - ''' + lower_status + '''
        4 - ''' + number_status + '''
        5 - ''' + special_status + '\n')

  if user == '1':
    new_length = input('type new length value\n')
    settings['length'] = int(new_length)
  elif user == '2':
    settings['UPPER'] = not settings['UPPER']
  elif user == '3':
    settings['lower'] = not settings['lower']
  elif user == '4':
    settings['numb6r'] = not settings['numb6r']
  elif user == '5':
    settings['speci@l'] = not settings['speci@l']
  