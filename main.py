from createDB import createDB
from entry_data import create_entry
import os



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
        print('1. [Aufräumarbeiten]'), print('2. [Installation & Einrichtung eines Laptops]'), print(
            '3. [First Level Support]')
        task_choice = input('Choose a Task or write down your own: ')
        if task_choice == '1':
            task_choice = '1.Aufräumarbeiten'
            return task_choice
        elif task_choice == '2':
            task_choice = '2. Installation & Einrichtung eines Laptops'
            return task_choice
        elif task_choice == '3':
            task_choice = 'First Level Support' + input('Type of Support: ')
            self.fls_status = 1
            return task_choice
        else:
            return task_choice

    def prntmenu(self):
        print('1. Create Entry')
        print('2. Delete Entry')
        print('3. Show Database')
        print('4. Exit')

        menu_choice = input('What would you like to do?: ')

        if menu_choice == '1':
            ce = create_entry(self.choose_task(), self.check_time(), self.fls_status)
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

