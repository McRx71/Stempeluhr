from createDB import createDB
from entry_data import create_entry
import os


def check_input():
    time = input('The Time it took: ')
    while type(time) == int:
            print('This must be an integer!')
            time = input('The Time it took: ')
            return time
    else:
        print('None')
        return time


class Menu:

    def prntmenu():
        print('1. Create Entry')
        print('2. Delete Entry')
        print('3. Show Database')
        print('4. Exit')

        menu_choice = input('What would you like to do?: ')

        if menu_choice == '1':
            print('Create Entry')
            ce = create_entry(check_input(), input('The Task: '))
            ce.write_data()
        elif menu_choice == '2':
            print('Delete Entry')
        elif menu_choice == '3':
            print('Show Database')
        elif menu_choice == '4' or 'exit':
            exit()

    def checkUp():
        createDB.checkDB()
    def clear():
        os.system('cls')

while True:
    Menu.clear()
    Menu.checkUp()
    Menu.prntmenu()

