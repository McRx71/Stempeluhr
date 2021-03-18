from  createDB import createDB
class Menu:

    def prntmenu():
        print('1. Create Entry')
        print('2. Delete Entry')
        print('3. Show Database')

        menu_choice = input('What would you like to do?: ')

        if menu_choice == '1':
            print('Create Entry')
        elif menu_choice == '2':
            print('Delete Entry')
        elif menu_choice == '3':
            print('Show Database')

    def checkUp():
        createDB.checkDB()
Menu.checkUp()
#Menu.prntmenu()

