from createDB import checkDB
from entry_data import create_entry
import os
from sys import platform



class Menu:

    def __init__(self, fls_status):
        self.fls_status = fls_status

    def check_time(self):
        check = False
        time = input('The Time it took: ')
        while check != True:
            if type(time) == int:
                print('This must be an integer!')
                time = input('The Time it took: ')
                return time
            else:
                check = True
                print('None')
                return time

    def choose_task(self):
        print('1. [Aufräumarbeiten]'), print('2. [Installation & Einrichtung eines Laptops]'), print('3. [First Level Support]')
        self.task_choice = input('Choose a Task or write down your own: ')
        if self.task_choice == '1':
            self.task_choice = 'Aufräumarbeiten'
            return self.task_choice
        elif self.task_choice == '2':
            self.task_choice = 'Installation & Einrichtung eines Laptops'
            return self.task_choice
        elif self.task_choice == '3':
            self.task_choice = 'First Level Support: ' + input('Type of Support: ')
            self.fls_status = '1'
            return self.task_choice
        elif self.task_choice == '4':
            self.task_choice = input('Your own task: ')
            return self.task_choice
        else:
            return self.task_choice

    def prntmenu(self):
        checkDB()
        print('1. Create Entry')
        print('2. Delete Entry')
        print('3. Show Database')
        print('4. Exit')

        self.menu_choice = input('What would you like to do?: ')
        if self.menu_choice == '1':
            ce = create_entry(self.choose_task(), self.check_time(), self.fls_status)
            print(ce)
            ce.write_data()
        elif self.menu_choice == '2':
            print('Delete Entry')
        elif self.menu_choice == '3':
            print('Show Database')
        elif self.menu_choice == '4' or 'exit':
            exit()

        if platform == "linux" or platform == "linux2":
            os.system('clear')
        elif platform == "win32":
            os.system('cls')
    def clear(self):
        os.system('cls')

while True:
    m = Menu(fls_status='0')
    m.prntmenu()

