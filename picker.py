import os
import random

#varables and functions
main_list = []
user_is_quit = False

def put_in_new_item():
    os.system('clear')
    print('are you sure you want to add a new item? \n1. yes\n2. no')
    temp_input = input('')

    if temp_input == '1':
        new_word = input('please input your new item:\n')
        main_list.append(new_word)
    elif temp_input == 2:
        pass

def show_current_list():
    os.system('clear')
    for item in main_list:
        print('item')
        temp_input = input('this is the current list\n1. back')
        if temp_input == '1':
            pass

def pull_random_item():
    os.system('clear')

def empty_list():
    os.system('clear')1

#code
while user_is_quit == False:
    os.system('clear')
    print('please choose a option \n1. put a new item into the list \n2. see current list \n3. pull out a random item from the list \n4. empty out list\n5. quit')
    temp_input = input('')

    if temp_input == '1':
        put_in_new_item()
    elif temp_input == '2':
        pass
    elif temp_input == '3':
        pass
    elif temp_input == '4':
        pass
    elif temp_input == '5':
        print('thank for using')
        user_is_quit = True