from itertools import count
import Model
import View



def main_menu():
    while True:
        print('\nГлавное меню:')
        print('1. Добавить контакт')
        print('2. Удалить контакт')
        print('3. Изменить контакт')
        print('4. Показать все контакты')
        print('5. Поиск по ФИО')
        print('6. Сохранить файл')
        print('0. Выйти из программы')
        choice = int(input('Выберите пункт: '))
        match (choice):
            case 1:
                add_contact()
                print('\nКонтакт добавлен\n')
            case 2:
                remove_contact()
                print('\nКонтакт удален\n')
            case 3:
                change_contact()
            case 4:
                print('\nВсе контакты:')
                show_contacts()
            case 5:
                search_surname()
                print('\nПоиск по ФИО\n')  
            case 6:
                save_file()
                print('\nФайл сохранен!\n')
            case 0:
                break


def start():
    
    main_menu()

def show_contacts():
    open_file()
    View.printPhoneBook()

def open_file():
    with open(Model.path, "r", encoding="UTF-8") as data:
        contacts_list = data.read().split("\n")
        Model.phonebook = contacts_list

def search_surname():
    surname = input("Введите фамилию или люыбе данные из ФИО: ")
    with open(Model.path, "r", encoding="UTF-8") as data:
        contacts_list = data.read().split("\n")
        Model.phonebook = contacts_list
        for line in contacts_list:
            count=0
            if surname in line:
                print(line)
                count+=1

def save_file():
    with open(Model.path, "w", encoding="UTF-8") as data:
        data.write(('\n'.join(Model.phonebook)))

def add_contact():
    name = input('Введите имя: ')
    surname = input('Введите фамилию: ')
    last_name = input('Введите отчество: ')
    phone = input('Введите телефон: ')
    contact = f'{name}; {surname}; {last_name}; {phone};\n'
    Model.phonebook.append(contact)
    View.printPhoneBook()

def remove_contact():
    choice = int(input('Введите номер элемента для удаления: '))
    Model.phonebook.pop(choice)
    View.printPhoneBook()

def change_contact():

    choice = int(input('Введите номер элемента для изменения: '))
    choice2 = int(input('Что изменяем (0-имя, 1-фамилия, 2-отчество, 3-телефон): '))

    contact = Model.phonebook.pop(choice).split(';')
    print(contact)
    contact[choice2] = input('Введите новое значение: ')
    print(contact)
    Model.phonebook.insert(choice, ';'.join(contact))
    View.printPhoneBook()