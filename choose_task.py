from types import CodeType


def choose_task_match(task_choice):
    #task_choice = input('Choose a Task or write down your own: ')
    print('Before Match: ' + task_choice)
    match task_choice:

        case 1:
            print('Case 1')
            task_choice = 'Aufräumarbeiten'
            print(task_choice)
            return  task_choice
        case 2:
            print('Case 2')
            task_choice = 'Installation & Einrichtung eines Laptops'
            print(task_choice)
            return task_choice  
        case 3:
            print('Case 3')
            task_choice = 'First Level Support: ' + input('Type of Support: ')
            fls_status = '1'
            return task_choice,fls_status
        case 4:
            print('Case 4')
            task_choice = input('Your own task: ')
            print(task_choice)
            return task_choice 
        case _:
            print('Default Case')
            task_choice = input('Your own task: ')
            print(task_choice)
            return task_choice 


print('1. [Aufräumarbeiten]'), print('2. [Installation & Einrichtung eines Laptops]'), print('3. [First Level Support]')
menu = input('Choose a Task or write down your own: ')
choose_task_match(menu)


def match_test(code):
    match code:

        case 22:
            print(22)
        case 33:
            print(33)
        case _:
            print('other shit')

match_test(22)