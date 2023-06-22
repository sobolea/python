import os

def show_contacts(file_name):
    os.system('CLS')
    with open(file_name, 'r') as file:
        data = file.readlines()
        for contact in data:
            print(contact, end='')
    input('\npress any key')

def add_contacts(file_name):
    os.system('CLS')
    with open(file_name, 'a') as file:
        res = '\n'
        res += input('input surname: ') + ' '
        res += input('input name: ') + ' '
        res += input('input number: ') + ' '
        file.write(res)
    input('contact was sucessfully added. Press any key to continue')

def search_contacts(file_name):
    os.system('CLS')
    target = input('input a name of contact fot searching: ')

    with open(file_name, 'r') as file:
        contacts =file.readlines()
        for contact in contacts:
            if target in contact:
                print(contact)
                break
        else :
            print('no contacts with this name')
    input('press any key')

def change_contacts(file_name):
    os.system('CLS')
    target = input('input a name of contact for changing: ')

    with open(file_name, 'r+') as file:
        contacts =file.readlines()
        new_contacts = []
        flg = True
        for contact in contacts:
            if target in contact:
                new_contacts.append(input('input new contact: ') + ' \n')
                print()
            else :
                new_contacts.append(contact)
        if new_contacts == contacts :
            print('no contacts with this name')
            flg = False
    if flg:
        with open(file_name, 'w') as file:
            file.writelines(new_contacts)

    input('press any key')


def delete_contacts(file_name):
    os.system('CLS')
    target = input('input a name of contact for deleting: ')

    with open(file_name, 'r+') as file:
        contacts =file.readlines()
        new_contacts = []
        flg = True
        for contact in contacts:
            if target not in contact:
                new_contacts.append(contact)
        if new_contacts == contacts :
            print('no contacts with this name')
            flg = False
    if flg:
        with open(file_name, 'w') as file:
            file.writelines(new_contacts)

    input('press any key')

def drawing():
    print('1 - show contacts')
    print('2 - add contact')
    print('3 - search contact')
    print('4 - delete contact')
    print('5 - change contact')
    print('6 - exit')

def main(file_name):
    while True:
        os.system('CLS')
        drawing()
        user_choice = int(input('input a number from 1 to 6: '))

        if user_choice == 1:
            show_contacts(file_name)
        elif user_choice == 2:
            add_contacts(file_name)
        elif user_choice == 3:
            search_contacts(file_name)
        elif user_choice == 4 :
            delete_contacts(file_name)
        elif user_choice == 5:
            change_contacts(file_name)
        elif user_choice ==6 :
            print('have a nice day')
        
            return

main('test.txt')